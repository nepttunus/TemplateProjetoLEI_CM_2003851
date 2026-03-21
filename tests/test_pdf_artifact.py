import json
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from src.capture import capture_url


HTML_PAGE = b"""<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>PDF Capture Page</title>
  </head>
  <body>
    <h1>PDF Capture</h1>
    <p>PDF artifact generation test.</p>
  </body>
</html>
"""


class PdfCaptureHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(HTML_PAGE)))
        self.end_headers()
        self.wfile.write(HTML_PAGE)

    def log_message(self, format, *args):
        return


def start_test_server():
    server = HTTPServer(("127.0.0.1", 0), PdfCaptureHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server, thread


def test_capture_creates_pdf_artifact(tmp_path):
    server, thread = start_test_server()

    try:
        host, port = server.server_address
        url = f"http://{host}:{port}/"

        result = capture_url(
            url=url,
            output_dir=tmp_path,
            timeout_ms=10000,
            headless=True,
        )

        pdf_path = result.artifacts_dir / "page.pdf"
        metadata_path = result.artifacts_dir / "capture_metadata.json"

        assert pdf_path.exists()
        assert pdf_path.stat().st_size > 0

        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        assert metadata["pdf_file"] == "artifacts/page.pdf"

    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)
