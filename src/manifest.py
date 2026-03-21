from __future__ import annotations

import json
import mimetypes
from datetime import datetime, timezone
from pathlib import Path

try:
    from hashing import sha256_file
except ModuleNotFoundError:
    from src.hashing import sha256_file


MANIFEST_FILENAME = "manifest.json"


def relative_to_run(run_dir: Path, file_path: Path) -> str:
    return file_path.relative_to(run_dir).as_posix()


def iso_utc_from_timestamp(timestamp: float) -> str:
    return datetime.fromtimestamp(timestamp, tz=timezone.utc).isoformat()


def infer_artifact_type(file_path: Path) -> str:
    name = file_path.name.lower()

    if name == "screenshot.png":
        return "screenshot"
    if name == "page.html":
        return "page-html"
    if name == "capture_metadata.json":
        return "capture-metadata"
    if name == "http_metadata.json":
        return "http-metadata"
    if name == "console_logs.json":
        return "console-logs"
    if name == "network.har":
        return "network-har"
    if name == "trace.zip":
        return "browser-trace"
    if name.endswith(".pdf"):
        return "page-pdf"

    return "artifact"


def build_file_entry(run_dir: Path, file_path: Path) -> dict:
    stat = file_path.stat()
    media_type, _ = mimetypes.guess_type(file_path.name)

    return {
        "path": relative_to_run(run_dir, file_path),
        "sha256": sha256_file(file_path),
        "size_bytes": stat.st_size,
        "modified_at": iso_utc_from_timestamp(stat.st_mtime),
        "artifact_type": infer_artifact_type(file_path),
        "media_type": media_type or "application/octet-stream",
        "filename": file_path.name,
    }


def build_manifest(run_dir: str | Path, capture_metadata: dict) -> tuple[dict, Path]:
    run_dir = Path(run_dir)
    artifacts_dir = run_dir / "artifacts"

    files = []
    for file_path in sorted(artifacts_dir.rglob("*")):
        if file_path.is_file():
            files.append(build_file_entry(run_dir, file_path))

    manifest = {
        "schema_version": "0.2.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "run_directory": run_dir.name,
        "capture": capture_metadata,
        "summary": {
            "file_count": len(files),
            "total_size_bytes": sum(item["size_bytes"] for item in files),
        },
        "files": files,
    }

    manifest_path = run_dir / MANIFEST_FILENAME
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    return manifest, manifest_path
