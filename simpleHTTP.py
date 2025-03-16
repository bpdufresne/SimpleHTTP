import http.server
import socketserver
import socket

PORT = 80
DIRECTORY = "./www"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Hosting {DIRECTORY} from this device on port: {PORT}")
    httpd.serve_forever()