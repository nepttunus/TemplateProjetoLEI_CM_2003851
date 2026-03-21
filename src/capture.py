from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

from playwright.sync_api import sync_playwright


@dataclass
class CaptureResult:
    run_dir: Path
    artifacts_dir: Path
    screenshot_path: Path
    html_path: Path
    metadata_path: Path
    http_metadata_path: Path
    console_logs_path: Path
    har_path: Path
    trace_path: Path
    capture_metadata: dict


def utc_now_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def slug_from_url(url: str) -> str:
    parsed = urlparse(url)
    base = parsed.netloc or parsed.path or "capture"
    slug = re.sub(r"[^a-zA-Z0-9._-]+", "_", base).strip("_")
    return slug or "capture"


def prepare_run_directories(base_output_dir: str | Path, url: str) -> tuple[Path, Path]:
    base_dir = Path(base_output_dir)
    run_dir = base_dir / f"{slug_from_url(url)}_{utc_now_compact()}"
    artifacts_dir = run_dir / "artifacts"
    artifacts_dir.mkdir(parents=True, exist_ok=False)
    return run_dir, artifacts_dir


def capture_url(url: str, output_dir: str | Path, timeout_ms: int = 30000, headless: bool = True) -> CaptureResult:
    run_dir, artifacts_dir = prepare_run_directories(output_dir, url)

    screenshot_path = artifacts_dir / "screenshot.png"
    html_path = artifacts_dir / "page.html"
    metadata_path = artifacts_dir / "capture_metadata.json"
    http_metadata_path = artifacts_dir / "http_metadata.json"
    console_logs_path = artifacts_dir / "console_logs.json"
    har_path = artifacts_dir / "network.har"
    trace_path = artifacts_dir / "trace.zip"

    capture_started_at = datetime.now(timezone.utc).isoformat()
    console_logs: list[dict] = []

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=headless)
        context = browser.new_context(
            ignore_https_errors=True,
            record_har_path=str(har_path),
            record_har_mode="full",
        )

        context.tracing.start(screenshots=True, snapshots=True, sources=True)

        page = context.new_page()

        def handle_console(msg) -> None:
            console_logs.append(
                {
                    "type": getattr(msg, "type", None),
                    "text": getattr(msg, "text", None),
                    "location": getattr(msg, "location", None),
                }
            )

        page.on("console", handle_console)

        response = page.goto(url, wait_until="networkidle", timeout=timeout_ms)
        page.screenshot(path=str(screenshot_path), full_page=True)
        html_path.write_text(page.content(), encoding="utf-8")

        capture_finished_at = datetime.now(timezone.utc).isoformat()
        title = page.title()

        response_headers = {}
        if response:
            try:
                response_headers = response.all_headers()
            except Exception:
                response_headers = {}

        http_metadata = {
            "source_url": url,
            "final_url": page.url,
            "page_title": title,
            "http_status": response.status if response else None,
            "response_headers": response_headers,
            "captured_at": capture_finished_at,
        }

        http_metadata_path.write_text(
            json.dumps(http_metadata, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

        console_logs_path.write_text(
            json.dumps(console_logs, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

        capture_metadata = {
            "source_url": url,
            "final_url": page.url,
            "page_title": title,
            "capture_started_at": capture_started_at,
            "capture_finished_at": capture_finished_at,
            "http_status": response.status if response else None,
            "browser": "chromium",
            "headless": headless,
            "timeout_ms": timeout_ms,
            "http_metadata_file": "artifacts/http_metadata.json",
            "console_logs_file": "artifacts/console_logs.json",
            "har_file": "artifacts/network.har",
            "trace_file": "artifacts/trace.zip",
        }

        metadata_path.write_text(
            json.dumps(capture_metadata, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

        context.tracing.stop(path=str(trace_path))
        context.close()
        browser.close()

    return CaptureResult(
        run_dir=run_dir,
        artifacts_dir=artifacts_dir,
        screenshot_path=screenshot_path,
        html_path=html_path,
        metadata_path=metadata_path,
        http_metadata_path=http_metadata_path,
        console_logs_path=console_logs_path,
        har_path=har_path,
        trace_path=trace_path,
        capture_metadata=capture_metadata,
    )
