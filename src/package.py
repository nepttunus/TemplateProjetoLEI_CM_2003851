from __future__ import annotations

from pathlib import Path
import zipfile


def create_zip_archive(run_dir: str | Path, zip_name: str = "evidence_bundle.zip") -> Path:
    run_dir = Path(run_dir)
    zip_path = run_dir / zip_name

    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for file_path in sorted(run_dir.rglob("*")):
            if file_path.is_file() and file_path != zip_path:
                zf.write(file_path, arcname=file_path.relative_to(run_dir.parent))

    return zip_path
