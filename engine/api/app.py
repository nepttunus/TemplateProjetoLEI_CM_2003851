from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from engine.src.service import run_capture_job

app = FastAPI(title="OSINT Evidence Capture Local API")


class CaptureRequest(BaseModel):
    url: str
    output_dir: str = "output"
    timeout_ms: int = 30000
    headless: bool = True
    actor: str = "browser_extension"


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/capture")
def capture(request: CaptureRequest):
    try:
        return run_capture_job(
            url=request.url,
            output_dir=request.output_dir,
            timeout_ms=request.timeout_ms,
            headless=request.headless,
            actor=request.actor,
        )
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
