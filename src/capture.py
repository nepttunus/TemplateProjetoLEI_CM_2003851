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

    capture_started_at = datetime.now(timezone.utc).isoformat()

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=headless)
        context = browser.new_context(ignore_https_errors=True)
        page = context.new_page()

        response = page.goto(url, wait_until="networkidle", timeout=timeout_ms)
        page.screenshot(path=str(screenshot_path), full_page=True)
        html_path.write_text(page.content(), encoding="utf-8")

        capture_finished_at = datetime.now(timezone.utc).isoformat()
        title = page.title()

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
        }

        metadata_path.write_text(
            json.dumps(capture_metadata, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

        context.close()
        browser.close()

    return CaptureResult(
        run_dir=run_dir,
        artifacts_dir=artifacts_dir,
        screenshot_path=screenshot_path,
        html_path=html_path,
        metadata_path=metadata_path,
        capture_metadata=capture_metadata,
    )
