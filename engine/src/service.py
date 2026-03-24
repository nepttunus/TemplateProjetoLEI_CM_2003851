from __future__ import annotations

from pathlib import Path

from .capture import capture_url
from .custody import write_chain_of_custody
from .manifest import build_manifest
from .package import create_zip_archive
from .reporting import write_report_json, write_report_markdown
from .signature import ensure_keypair, sign_manifest


def run_capture_job(
    url: str,
    output_dir: str | Path = "output",
    timeout_ms: int = 30000,
    headless: bool = True,
    actor: str = "system",
) -> dict:
    result = capture_url(
        url=url,
        output_dir=output_dir,
        timeout_ms=timeout_ms,
        headless=headless,
    )

    keys_dir = result.run_dir / "keys"
    private_key_path, public_key_path = ensure_keypair(keys_dir)

    custody_path = write_chain_of_custody(
        result.run_dir,
        result.capture_metadata,
        actor=actor,
        extra_events=[
            {
                "action": "keypair_generated",
                "target": "keys/public_key.pem",
                "details": {"algorithm": "Ed25519"},
            }
        ],
    )

    provisional_manifest, _ = build_manifest(result.run_dir, result.capture_metadata)

    report_json_path = write_report_json(
        result.run_dir,
        result.capture_metadata,
        provisional_manifest,
    )
    report_md_path = write_report_markdown(
        result.run_dir,
        result.capture_metadata,
        provisional_manifest,
    )

    manifest, manifest_path = build_manifest(result.run_dir, result.capture_metadata)

    signature_path = sign_manifest(
        manifest_path,
        private_key_path,
        result.run_dir / "manifest.sig",
    )

    zip_path = create_zip_archive(result.run_dir)

    payload = {
        "status": "ok",
        "message": "Capture completed successfully.",
        "run_dir": str(result.run_dir),
        "manifest": str(manifest_path),
        "signature": str(signature_path),
        "public_key": str(public_key_path),
        "chain_of_custody": str(custody_path),
        "report_json": str(report_json_path),
        "report_md": str(report_md_path),
        "zip": str(zip_path),
        "actor": actor,
        "files": [item["path"] for item in manifest["files"]],
    }

    return payload
