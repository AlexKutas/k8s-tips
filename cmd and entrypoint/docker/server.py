from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
import sys
import time

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'<b>Hello from hostname: %s <br><br>' % socket.gethostname().encode())
        self.wfile.write(b'<b>Timeout interval: </b> %s <br><br>' % str(timeout_interval).encode())
        self.wfile.write(b'<b>Desired Interval: </b> %s <br><br>' % str(desired_interval).encode())
        count = 1
        while count <= desired_interval:
            self.wfile.write(b'<b> %s. Current time: </b> %s<br>' % (str(count).encode(), str(time.strftime("%X")).encode()))
            time.sleep(timeout_interval)

            count += 1

        self.wfile.write(b'<br><b>Interval completed</b>')

timeout_interval = int(sys.argv[1])
desired_interval = int(sys.argv[2])

SERVER_PORT = 8000
httpd = HTTPServer(('0.0.0.0', SERVER_PORT), SimpleHTTPRequestHandler)
print(f'Starting server on http://localhost:{SERVER_PORT}')
httpd.serve_forever()
