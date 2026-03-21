import json
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from src.capture import capture_url


HTML_PAGE = b"""<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Trace Capture Page</title>
    <script>
      console.log("trace-test-ok");
    </script>
  </head>
  <body>
    <h1>Trace Capture</h1>
  </body>
</html>
"""


class TraceCaptureHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(HTML_PAGE)))
        self.end_headers()
        self.wfile.write(HTML_PAGE)

    def log_message(self, format, *args):
        return


def start_test_server():
    server = HTTPServer(("127.0.0.1", 0), TraceCaptureHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server, thread


def test_capture_creates_har_and_trace_artifacts(tmp_path):
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

        har_path = result.artifacts_dir / "network.har"
        trace_path = result.artifacts_dir / "trace.zip"
        metadata_path = result.artifacts_dir / "capture_metadata.json"

        assert har_path.exists()
        assert trace_path.exists()
        assert har_path.stat().st_size > 0
        assert trace_path.stat().st_size > 0

        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        assert metadata["har_file"] == "artifacts/network.har"
        assert metadata["trace_file"] == "artifacts/trace.zip"

    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)
