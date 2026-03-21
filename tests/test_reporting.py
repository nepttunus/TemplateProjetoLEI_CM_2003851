import json

from src.manifest import build_manifest
from src.reporting import write_report_json, write_report_markdown


def test_reporting_files_are_created(tmp_path):
    run_dir = tmp_path / "report_run"
    artifacts_dir = run_dir / "artifacts"
    artifacts_dir.mkdir(parents=True)

    html = artifacts_dir / "page.html"
    html.write_text("<html><title>Report Test</title></html>", encoding="utf-8")

    capture_metadata = {
        "source_url": "https://example.org",
        "final_url": "https://example.org/",
        "page_title": "Example Domain",
        "http_status": 200,
        "capture_started_at": "2026-03-21T01:00:00+00:00",
        "capture_finished_at": "2026-03-21T01:00:05+00:00",
    }

    manifest, _ = build_manifest(run_dir, capture_metadata)

    report_json = write_report_json(run_dir, capture_metadata, manifest)
    report_md = write_report_markdown(run_dir, capture_metadata, manifest)

    assert report_json.exists()
    assert report_md.exists()

    payload = json.loads(report_json.read_text(encoding="utf-8"))
    assert payload["run_directory"] == "report_run"
    assert payload["capture_summary"]["page_title"] == "Example Domain"
    assert payload["artifacts"]["count"] >= 1

    markdown = report_md.read_text(encoding="utf-8")
    assert "# Relatório Resumido da Execução" in markdown
    assert "Example Domain" in markdown
    assert "`artifacts/page.html`" in markdown
