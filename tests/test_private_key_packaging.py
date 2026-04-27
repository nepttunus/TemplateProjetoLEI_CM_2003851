from zipfile import ZipFile

from src.package import create_zip_archive


def test_evidence_zip_excludes_private_key(tmp_path):
    run_dir = tmp_path / "run_example"
    keys_dir = run_dir / "keys"
    keys_dir.mkdir(parents=True)

    (keys_dir / "private_key.pem").write_text("secret", encoding="utf-8")
    (keys_dir / "public_key.pem").write_text("public", encoding="utf-8")
    (run_dir / "manifest.json").write_text("{}", encoding="utf-8")

    zip_path = create_zip_archive(run_dir)

    with ZipFile(zip_path) as zf:
        names = set(zf.namelist())

    assert "run_example/keys/public_key.pem" in names
    assert "run_example/keys/private_key.pem" not in names
