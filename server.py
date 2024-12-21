#!/usr/bin/env python3
from os import getenv
from http.server import HTTPServer, BaseHTTPRequestHandler
from ping_host import is_host_reachable

PORT = getenv("MONITOR_SERVER_PORT", None)
if PORT is None:
    raise ValueError("MONITOR_SERVER_PORT environment variable must be set")

class RequestHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        """Check if the host is reachable and return 200 if it is, 503 otherwise"""
        if not is_host_reachable():
            self.send_response(503)
            self.send_header("Content-type", "text/html")
            self.end_headers()
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

def run_server():
    server = HTTPServer(
        server_address=("0.0.0.0", int(PORT)),
        RequestHandlerClass=RequestHandler,
    )
    print(f"Starting server on 0.0.0.0:{PORT}")
    server.serve_forever()

if __name__ == "__main__":
    run_server()

