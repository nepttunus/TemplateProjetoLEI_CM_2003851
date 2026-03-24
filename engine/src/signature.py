from __future__ import annotations

import base64
from pathlib import Path

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey,
    Ed25519PublicKey,
)


def ensure_keypair(keys_dir: str | Path = "keys") -> tuple[Path, Path]:
    keys_dir = Path(keys_dir)
    keys_dir.mkdir(parents=True, exist_ok=True)

    private_key_path = keys_dir / "private_key.pem"
    public_key_path = keys_dir / "public_key.pem"

    if private_key_path.exists() and public_key_path.exists():
        return private_key_path, public_key_path

    private_key = Ed25519PrivateKey.generate()
    public_key = private_key.public_key()

    private_key_path.write_bytes(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )
    )

    public_key_path.write_bytes(
        public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )
    )

    return private_key_path, public_key_path


def load_private_key(private_key_path: str | Path) -> Ed25519PrivateKey:
    return serialization.load_pem_private_key(
        Path(private_key_path).read_bytes(),
        password=None,
    )


def load_public_key(public_key_path: str | Path) -> Ed25519PublicKey:
    return serialization.load_pem_public_key(
        Path(public_key_path).read_bytes(),
    )


def sign_manifest(
    manifest_path: str | Path,
    private_key_path: str | Path,
    signature_path: str | Path | None = None,
) -> Path:
    manifest_path = Path(manifest_path)
    signature_path = Path(signature_path) if signature_path else manifest_path.with_suffix(".sig")

    private_key = load_private_key(private_key_path)
    signature = private_key.sign(manifest_path.read_bytes())
    signature_path.write_text(base64.b64encode(signature).decode("ascii"), encoding="utf-8")
    return signature_path


def verify_manifest_signature(
    manifest_path: str | Path,
    signature_path: str | Path,
    public_key_path: str | Path,
) -> bool:
    manifest_path = Path(manifest_path)
    signature_path = Path(signature_path)

    public_key = load_public_key(public_key_path)
    signature = base64.b64decode(signature_path.read_text(encoding="utf-8"))

    try:
        public_key.verify(signature, manifest_path.read_bytes())
        return True
    except Exception:
        return False
