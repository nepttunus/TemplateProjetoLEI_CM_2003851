import json

from src.custody import write_chain_of_custody
from src.manifest import build_manifest
from src.signature import ensure_keypair


def test_chain_of_custody_is_created_and_listed_in_manifest(tmp_path):
    run_dir = tmp_path / "custody_run"
    artifacts_dir = run_dir / "artifacts"
    artifacts_dir.mkdir(parents=True)

    html = artifacts_dir / "page.html"
    html.write_text("<html><title>Custody Test</title></html>", encoding="utf-8")

    capture_metadata = {
        "source_url": "https://example.org",
        "final_url": "https://example.org/",
        "page_title": "Example Domain",
        "http_status": 200,
        "capture_started_at": "2026-03-21T01:00:00+00:00",
        "capture_finished_at": "2026-03-21T01:00:05+00:00",
    }

    ensure_keypair(run_dir / "keys")

    chain_path = write_chain_of_custody(
        run_dir,
        capture_metadata,
        actor="tester",
        extra_events=[
            {
                "action": "keypair_generated",
                "target": "keys/public_key.pem",
                "details": {"algorithm": "Ed25519"},
            }
        ],
    )

    manifest, manifest_path = build_manifest(run_dir, capture_metadata)

    assert chain_path.exists()
    assert manifest_path.exists()

    chain = json.loads(chain_path.read_text(encoding="utf-8"))
    assert chain["schema_version"] == "0.1.0"
    assert len(chain["events"]) >= 3

    actions = [event["action"] for event in chain["events"]]
    assert "capture_started" in actions
    assert "capture_completed" in actions
    assert "keypair_generated" in actions

    paths = {item["path"] for item in manifest["files"]}
    assert "chain_of_custody.json" in paths
    assert "keys/public_key.pem" in paths
