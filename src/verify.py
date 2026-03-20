from __future__ import annotations

import json
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from zipfile import ZipFile

try:
    from hashing import sha256_file
except ModuleNotFoundError:
    from src.hashing import sha256_file


@dataclass
class VerificationResult:
    ok: bool
    checked_files: int
    errors: list[str] = field(default_factory=list)


def load_manifest(run_dir: Path) -> dict:
    manifest_path = run_dir / "manifest.json"
    if not manifest_path.exists():
        raise FileNotFoundError(f"Manifesto não encontrado: {manifest_path}")
    return json.loads(manifest_path.read_text(encoding="utf-8"))


def verify_run_directory(run_dir: str | Path) -> VerificationResult:
    run_dir = Path(run_dir)
    manifest = load_manifest(run_dir)

    errors: list[str] = []
    checked = 0

    for entry in manifest.get("files", []):
        expected_path = run_dir / entry["path"]
        expected_hash = entry["sha256"]

        if not expected_path.exists():
            errors.append(f"Ficheiro em falta: {entry['path']}")
            continue

        current_hash = sha256_file(expected_path)
        checked += 1

        if current_hash != expected_hash:
            errors.append(
                f"Hash inválido em {entry['path']}: esperado {expected_hash}, obtido {current_hash}"
            )

    return VerificationResult(ok=not errors, checked_files=checked, errors=errors)


def verify_path(path: str | Path) -> VerificationResult:
    path = Path(path)

    if path.is_dir():
        return verify_run_directory(path)

    if path.is_file() and path.suffix.lower() == ".zip":
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            with ZipFile(path, "r") as archive:
                archive.extractall(temp_path)
            return verify_run_directory(temp_path)

    raise ValueError("O caminho indicado deve ser uma pasta de evidência ou um ficheiro .zip")
