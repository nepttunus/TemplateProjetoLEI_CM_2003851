import json
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from src.capture import capture_url


HTML_PAGE = b"""<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Test Capture Page</title>
    <script>
      console.log("capture-test-ok");
    </script>
  </head>
  <body>
    <h1>Capture Test</h1>
  </body>
</html>
"""


class CaptureHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("X-Test-Header", "capture-artifacts")
        self.send_header("Content-Length", str(len(HTML_PAGE)))
        self.end_headers()
        self.wfile.write(HTML_PAGE)

    def log_message(self, format, *args):
        return


def start_test_server():
    server = HTTPServer(("127.0.0.1", 0), CaptureHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server, thread


def test_capture_creates_http_and_console_artifacts(tmp_path):
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

        http_metadata_path = result.artifacts_dir / "http_metadata.json"
        console_logs_path = result.artifacts_dir / "console_logs.json"

        assert http_metadata_path.exists()
        assert console_logs_path.exists()

        http_metadata = json.loads(http_metadata_path.read_text(encoding="utf-8"))
        console_logs = json.loads(console_logs_path.read_text(encoding="utf-8"))

        assert http_metadata["source_url"] == url
        assert http_metadata["final_url"].startswith(url)
        assert http_metadata["page_title"] == "Test Capture Page"
        assert http_metadata["http_status"] == 200
        assert http_metadata["response_headers"]["x-test-header"] == "capture-artifacts"

        assert any(
            "capture-test-ok" in (entry.get("text") or "")
            for entry in console_logs
        )

        assert result.capture_metadata["http_metadata_file"] == "artifacts/http_metadata.json"
        assert result.capture_metadata["console_logs_file"] == "artifacts/console_logs.json"

    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)
