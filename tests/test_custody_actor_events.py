import json

from src.cli import build_parser
from src.custody import write_chain_of_custody
from src.signature import ensure_keypair


def test_cli_capture_accepts_actor_argument():
    parser = build_parser()
    args = parser.parse_args(["capture", "https://example.org", "--actor", "Carlos"])
    assert args.actor == "Carlos"


def test_chain_of_custody_records_actor_and_extended_events(tmp_path):
    run_dir = tmp_path / "custody_actor_run"
    artifacts_dir = run_dir / "artifacts"
    artifacts_dir.mkdir(parents=True)

    ensure_keypair(run_dir / "keys")

    capture_metadata = {
        "source_url": "https://example.org",
        "final_url": "https://example.org/",
        "page_title": "Example Domain",
        "http_status": 200,
        "capture_started_at": "2026-03-21T02:00:00+00:00",
        "capture_finished_at": "2026-03-21T02:00:05+00:00",
    }

    chain_path = write_chain_of_custody(
        run_dir,
        capture_metadata,
        actor="Carlos",
        extra_events=[
            {
                "action": "keypair_generated",
                "target": "keys/public_key.pem",
                "details": {"algorithm": "Ed25519"},
            },
            {
                "action": "manifest_created",
                "target": "manifest.json",
            },
            {
                "action": "report_generated",
                "target": "report.json",
                "details": {"formats": ["json", "markdown"]},
            },
            {
                "action": "manifest_signed",
                "target": "manifest.sig",
            },
            {
                "action": "package_created",
                "target": "evidence_bundle.zip",
            },
        ],
    )

    chain = json.loads(chain_path.read_text(encoding="utf-8"))
    events = chain["events"]

    assert len(events) >= 7
    assert all(event["actor"] == "Carlos" for event in events)

    actions = [event["action"] for event in events]
    assert "capture_started" in actions
    assert "capture_completed" in actions
    assert "keypair_generated" in actions
    assert "manifest_created" in actions
    assert "report_generated" in actions
    assert "manifest_signed" in actions
    assert "package_created" in actions
