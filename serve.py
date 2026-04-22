from http.server import HTTPServer, SimpleHTTPRequestHandler
import mimetypes
import os

class UnityWebGLHandler(SimpleHTTPRequestHandler):

    def end_headers(self):
        path = self.path

        if path.endswith(".br"):
            self.send_header("Content-Encoding", "br")

        elif path.endswith(".gz"):
            self.send_header("Content-Encoding", "gzip")

        super().end_headers()

    def guess_type(self, path):
        if path.endswith(".wasm"):
            return "application/wasm"
        if path.endswith(".js"):
            return "application/javascript"
        return super().guess_type(path)

if __name__ == "__main__":
    mimetypes.init()
    server = HTTPServer(("localhost", 8000), UnityWebGLHandler)
    print("✅ Unity WebGL server running on http://localhost:8000")
    server.serve_forever()