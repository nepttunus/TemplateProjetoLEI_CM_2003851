from __future__ import annotations

import json
from pathlib import Path

from src.capture import capture_url
from src.cli import build_parser
from src.custody import write_chain_of_custody
from src.manifest import build_manifest
from src.package import create_zip_archive
from src.signature import ensure_keypair, sign_manifest
from src.verify import verify_path


def cmd_capture(args):
    result = capture_url(
        url=args.url,
        output_dir=args.output_dir,
        timeout_ms=args.timeout_ms,
        headless=not getattr(args, "headed", False),
    )

    keys_dir = result.run_dir / "keys"
    private_key_path, public_key_path = ensure_keypair(keys_dir)

    custody_path = write_chain_of_custody(
        result.run_dir,
        result.capture_metadata,
        actor="system",
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
        "run_dir": str(result.run_dir),
        "manifest": str(manifest_path),
        "signature": str(signature_path),
        "public_key": str(public_key_path),
        "chain_of_custody": str(custody_path),
        "zip": str(zip_path),
        "files": [item["path"] for item in manifest["files"]],
    }
    print(json.dumps(payload, indent=2, ensure_ascii=False))


def cmd_verify(args):
    result = verify_path(Path(args.target))
    print(
        json.dumps(
            {
                "status": "ok" if result.ok else "error",
                "checked_files": result.checked_files,
                "errors": result.errors,
            },
            indent=2,
            ensure_ascii=False,
        )
    )


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "capture":
        cmd_capture(args)
    elif args.command == "verify":
        cmd_verify(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
