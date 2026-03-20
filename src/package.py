from __future__ import annotations

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


def create_zip_archive(run_dir: str | Path, zip_name: str = "evidence_bundle.zip") -> Path:
    run_dir = Path(run_dir)
    zip_path = run_dir / zip_name

    with ZipFile(zip_path, mode="w", compression=ZIP_DEFLATED) as archive:
        for path in sorted(run_dir.rglob("*")):
            if path.is_file() and path != zip_path:
                archive.write(path, arcname=path.relative_to(run_dir).as_posix())

    return zip_path
