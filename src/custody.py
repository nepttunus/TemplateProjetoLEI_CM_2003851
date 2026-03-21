from __future__ import annotations

import json
import uuid
from datetime import datetime, timezone
from pathlib import Path


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def build_event(
    action: str,
    actor: str,
    target: str,
    details: dict | None = None,
    timestamp: str | None = None,
) -> dict:
    return {
        "event_id": str(uuid.uuid4()),
        "timestamp": timestamp or utc_now_iso(),
        "action": action,
        "actor": actor,
        "target": target,
        "details": details or {},
    }


def write_chain_of_custody(
    run_dir: str | Path,
    capture_metadata: dict,
    actor: str = "system",
) -> Path:
    run_dir = Path(run_dir)
    chain_path = run_dir / "chain_of_custody.json"

    source_url = capture_metadata.get("source_url", "")
    final_url = capture_metadata.get("final_url", source_url)

    events = [
        build_event(
            action="capture_started",
            actor=actor,
            target=source_url,
            details={"run_directory": run_dir.name},
            timestamp=capture_metadata.get("capture_started_at"),
        ),
        build_event(
            action="capture_completed",
            actor=actor,
            target=final_url,
            details={
                "page_title": capture_metadata.get("page_title"),
                "http_status": capture_metadata.get("http_status"),
            },
            timestamp=capture_metadata.get("capture_finished_at"),
        ),
        build_event(
            action="keypair_generated",
            actor=actor,
            target="keys/public_key.pem",
            details={"algorithm": "Ed25519"},
        ),
    ]

    payload = {
        "schema_version": "0.1.0",
        "generated_at": utc_now_iso(),
        "run_directory": run_dir.name,
        "events": events,
    }

    chain_path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    return chain_path
