from __future__ import annotations

import json

try:
    from capture import capture_url
    from cli import build_parser
    from manifest import build_manifest
    from package import create_zip_archive
    from verify import verify_path
except ModuleNotFoundError:
    from src.capture import capture_url
    from src.cli import build_parser
    from src.manifest import build_manifest
    from src.package import create_zip_archive
    from src.verify import verify_path


def run_capture(args) -> int:
    result = capture_url(
        url=args.url,
        output_dir=args.output_dir,
        timeout_ms=args.timeout_ms,
        headless=args.headless,
    )

    manifest, manifest_path = build_manifest(
        run_dir=result.run_dir,
        capture_metadata=result.capture_metadata,
    )
    zip_path = create_zip_archive(result.run_dir)

    print(json.dumps(
        {
            "status": "ok",
            "run_dir": str(result.run_dir),
            "manifest": str(manifest_path),
            "zip": str(zip_path),
            "files": [item["path"] for item in manifest["files"]],
        },
        indent=2,
        ensure_ascii=False,
    ))
    return 0


def run_verify(args) -> int:
    verification = verify_path(args.path)

    payload = {
        "status": "ok" if verification.ok else "failed",
        "checked_files": verification.checked_files,
        "errors": verification.errors,
    }
    print(json.dumps(payload, indent=2, ensure_ascii=False))
    return 0 if verification.ok else 1


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "capture":
        return run_capture(args)
    if args.command == "verify":
        return run_verify(args)

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
