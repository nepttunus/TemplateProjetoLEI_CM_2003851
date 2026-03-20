from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

try:
    from hashing import sha256_file
except ModuleNotFoundError:
    from src.hashing import sha256_file


MANIFEST_FILENAME = "manifest.json"


def relative_to_run(run_dir: Path, file_path: Path) -> str:
    return file_path.relative_to(run_dir).as_posix()


def build_manifest(run_dir: str | Path, capture_metadata: dict) -> tuple[dict, Path]:
    run_dir = Path(run_dir)
    artifacts_dir = run_dir / "artifacts"

    files = []
    for file_path in sorted(artifacts_dir.rglob("*")):
        if file_path.is_file():
            files.append(
                {
                    "path": relative_to_run(run_dir, file_path),
                    "sha256": sha256_file(file_path),
                    "size_bytes": file_path.stat().st_size,
                }
            )

    manifest = {
        "schema_version": "0.1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "capture": capture_metadata,
        "files": files,
    }

    manifest_path = run_dir / MANIFEST_FILENAME
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    return manifest, manifest_path
