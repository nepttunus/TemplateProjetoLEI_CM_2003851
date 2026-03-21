from __future__ import annotations

import json
from pathlib import Path

from src.manifest import build_manifest


def test_build_manifest_includes_richer_file_metadata(tmp_path):
    run_dir = tmp_path / "run_example"
    artifacts_dir = run_dir / "artifacts"
    artifacts_dir.mkdir(parents=True)

    screenshot = artifacts_dir / "screenshot.png"
    screenshot.write_bytes(b"fake-png-data")

    html = artifacts_dir / "page.html"
    html.write_text("<html><title>Test</title></html>", encoding="utf-8")

    capture_metadata = {
        "source_url": "https://example.org",
        "final_url": "https://example.org/",
        "page_title": "Example Domain",
        "http_status": 200,
    }

    manifest, manifest_path = build_manifest(run_dir, capture_metadata)

    assert manifest_path.exists()
    assert manifest["schema_version"] == "0.2.0"
    assert manifest["run_directory"] == "run_example"
    assert manifest["summary"]["file_count"] == 2
    assert manifest["summary"]["total_size_bytes"] > 0

    files_by_path = {item["path"]: item for item in manifest["files"]}

    screenshot_entry = files_by_path["artifacts/screenshot.png"]
    assert screenshot_entry["artifact_type"] == "screenshot"
    assert screenshot_entry["media_type"] == "image/png"
    assert screenshot_entry["filename"] == "screenshot.png"
    assert screenshot_entry["size_bytes"] > 0
    assert "modified_at" in screenshot_entry
    assert "sha256" in screenshot_entry

    html_entry = files_by_path["artifacts/page.html"]
    assert html_entry["artifact_type"] == "page-html"
    assert html_entry["media_type"] == "text/html"
    assert html_entry["filename"] == "page.html"

    saved_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert saved_manifest["summary"]["file_count"] == 2
