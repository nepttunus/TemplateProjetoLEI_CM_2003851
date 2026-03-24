from __future__ import annotations

import json
from pathlib import Path

from .cli import build_parser
from .service import run_capture_job
from .verify import verify_path


def cmd_capture(args):
    payload = run_capture_job(
        url=args.url,
        output_dir=args.output_dir,
        timeout_ms=args.timeout_ms,
        headless=not getattr(args, "headed", False),
        actor=args.actor,
    )
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
