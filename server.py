from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello World")

PORT = 8000

server = HTTPServer(("0.0.0.0", PORT), HelloHandler)

print(f"Server running on http://0.0.0.0:{PORT}")

server.serve_forever()
