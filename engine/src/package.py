from __future__ import annotations

from pathlib import Path
import zipfile


def create_zip_archive(
    run_dir: str | Path,
    zip_name: str = "evidence_bundle.zip",
    exclude_names: set[str] | None = None,
) -> Path:
    run_dir = Path(run_dir)
    zip_path = run_dir / zip_name
    excluded = exclude_names or {"private_key.pem", "_private_keys"}

    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for file_path in sorted(run_dir.rglob("*")):
            if not file_path.is_file() or file_path == zip_path:
                continue
            if file_path.name in excluded or any(part in excluded for part in file_path.parts):
                continue
            zf.write(file_path, arcname=file_path.relative_to(run_dir.parent))

    return zip_path
