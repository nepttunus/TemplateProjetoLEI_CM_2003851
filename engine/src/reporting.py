from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def build_report_payload(run_dir: Path, capture_metadata: dict, manifest: dict) -> dict:
    files = manifest.get("files", [])
    artifact_paths = [item["path"] for item in files]

    return {
        "schema_version": "0.1.0",
        "generated_at": utc_now_iso(),
        "run_directory": run_dir.name,
        "capture_summary": {
            "source_url": capture_metadata.get("source_url"),
            "final_url": capture_metadata.get("final_url"),
            "page_title": capture_metadata.get("page_title"),
            "http_status": capture_metadata.get("http_status"),
            "capture_started_at": capture_metadata.get("capture_started_at"),
            "capture_finished_at": capture_metadata.get("capture_finished_at"),
        },
        "artifacts": {
            "count": len(files),
            "paths": artifact_paths,
        },
        "integrity": {
            "manifest_file": "manifest.json",
            "signature_file": "manifest.sig",
        },
    }


def write_report_json(run_dir: str | Path, capture_metadata: dict, manifest: dict) -> Path:
    run_dir = Path(run_dir)
    report_path = run_dir / "report.json"
    payload = build_report_payload(run_dir, capture_metadata, manifest)
    report_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    return report_path


def write_report_markdown(run_dir: str | Path, capture_metadata: dict, manifest: dict) -> Path:
    run_dir = Path(run_dir)
    report_path = run_dir / "report.md"

    files = manifest.get("files", [])
    artifact_lines = "\n".join(f"- `{item['path']}`" for item in files)

    markdown = f"""# Relatório Resumido da Execução

## Identificação

- **Run directory:** `{run_dir.name}`
- **Source URL:** {capture_metadata.get("source_url")}
- **Final URL:** {capture_metadata.get("final_url")}
- **Título da página:** {capture_metadata.get("page_title")}
- **HTTP status:** {capture_metadata.get("http_status")}

## Captura

- **Início:** {capture_metadata.get("capture_started_at")}
- **Fim:** {capture_metadata.get("capture_finished_at")}

## Integridade

- **Manifesto:** `manifest.json`
- **Assinatura:** `manifest.sig`

## Artefactos incluídos

{artifact_lines}
"""
    report_path.write_text(markdown, encoding="utf-8")
    return report_path
