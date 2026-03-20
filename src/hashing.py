from __future__ import annotations

import hashlib
from pathlib import Path


CHUNK_SIZE = 1024 * 1024


def sha256_file(file_path: str | Path) -> str:
    path = Path(file_path)
    digest = hashlib.sha256()

    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(CHUNK_SIZE), b""):
            digest.update(chunk)

    return digest.hexdigest()
