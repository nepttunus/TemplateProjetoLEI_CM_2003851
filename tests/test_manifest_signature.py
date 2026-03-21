import json

from src.manifest import build_manifest
from src.signature import ensure_keypair, sign_manifest
from src.verify import verify_path


def test_verify_accepts_signed_manifest(tmp_path):
    run_dir = tmp_path / "signed_run"
    artifacts_dir = run_dir / "artifacts"
    artifacts_dir.mkdir(parents=True)

    artifact = artifacts_dir / "page.html"
    artifact.write_text("<html>signed</html>", encoding="utf-8")

    capture_metadata = {
        "source_url": "https://example.org",
        "final_url": "https://example.org/",
        "page_title": "Example Domain",
        "http_status": 200,
    }

    _, manifest_path = build_manifest(run_dir, capture_metadata)

    keys_dir = run_dir / "keys"
    private_key_path, _ = ensure_keypair(keys_dir)
    sign_manifest(manifest_path, private_key_path, run_dir / "manifest.sig")

    result = verify_path(run_dir)

    assert result.ok is True
    assert result.checked_files == 1
    assert result.errors == []


def test_verify_rejects_tampered_signed_manifest(tmp_path):
    run_dir = tmp_path / "tampered_signed_run"
    artifacts_dir = run_dir / "artifacts"
    artifacts_dir.mkdir(parents=True)

    artifact = artifacts_dir / "page.html"
    artifact.write_text("<html>original</html>", encoding="utf-8")

    capture_metadata = {
        "source_url": "https://example.org",
        "final_url": "https://example.org/",
        "page_title": "Example Domain",
        "http_status": 200,
    }

    _, manifest_path = build_manifest(run_dir, capture_metadata)

    keys_dir = run_dir / "keys"
    private_key_path, _ = ensure_keypair(keys_dir)
    sign_manifest(manifest_path, private_key_path, run_dir / "manifest.sig")

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["capture"]["page_title"] = "Tampered Title"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    result = verify_path(run_dir)

    assert result.ok is False
    assert any("Assinatura do manifesto inválida" in error for error in result.errors)
