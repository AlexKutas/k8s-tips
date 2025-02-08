from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
import sys
import time

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'<b>Hello from hostname: %s <br><br>' % socket.gethostname().encode())
        self.wfile.write(b'<b>Text argument: </b> %s <br><br>' % str(text_argument).encode())

text_argument = str(sys.argv[1])

SERVER_PORT = 8000
httpd = HTTPServer(('0.0.0.0', SERVER_PORT), SimpleHTTPRequestHandler)
print(f'Starting server on http://localhost:{SERVER_PORT}')
httpd.serve_forever()
