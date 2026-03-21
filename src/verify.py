from __future__ import annotations

import json
import shutil
import tempfile
import zipfile
from dataclasses import dataclass
from pathlib import Path

from src.hashing import sha256_file
from src.signature import verify_manifest_signature


@dataclass
class VerifyResult:
    ok: bool
    checked_files: int
    errors: list[str]


def verify_run_directory(run_dir: Path) -> VerifyResult:
    manifest_path = run_dir / "manifest.json"
    if not manifest_path.exists():
        return VerifyResult(False, 0, ["Manifest não encontrado"])

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    errors: list[str] = []
    checked_files = 0

    for entry in manifest.get("files", []):
        file_path = run_dir / entry["path"]
        if not file_path.exists():
            errors.append(f"Ficheiro em falta: {entry['path']}")
            continue

        current_hash = sha256_file(file_path)
        if current_hash != entry["sha256"]:
            errors.append(f"Hash inválido: {entry['path']}")
        checked_files += 1

    signature_path = run_dir / "manifest.sig"
    public_key_path = run_dir / "keys" / "public_key.pem"

    if signature_path.exists():
        if not public_key_path.exists():
            errors.append("Chave pública em falta para validar assinatura")
        else:
            if not verify_manifest_signature(manifest_path, signature_path, public_key_path):
                errors.append("Assinatura do manifesto inválida")

    return VerifyResult(len(errors) == 0, checked_files, errors)


def verify_zip(zip_path: Path) -> VerifyResult:
    with tempfile.TemporaryDirectory() as tmp_dir:
        extract_dir = Path(tmp_dir) / "extracted"
        extract_dir.mkdir(parents=True, exist_ok=True)

        with zipfile.ZipFile(zip_path, "r") as zf:
            zf.extractall(extract_dir)

        entries = [p for p in extract_dir.iterdir()]
        if len(entries) == 1 and entries[0].is_dir():
            return verify_run_directory(entries[0])

        return verify_run_directory(extract_dir)


def verify_path(target: str | Path) -> VerifyResult:
    target = Path(target)

    if not target.exists():
        return VerifyResult(False, 0, [f"Caminho não encontrado: {target}"])

    if target.is_file() and target.suffix.lower() == ".zip":
        return verify_zip(target)

    if target.is_dir():
        return verify_run_directory(target)

    return VerifyResult(False, 0, [f"Formato não suportado: {target}"])
