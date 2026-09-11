import http.server
import socketserver
import os
import sys

PORT = 8085
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class SPAServerHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        # Strip query and hash to find file
        clean_path = self.path.split('?')[0].split('#')[0]
        full_path = self.translate_path(clean_path)
        
        # If the file does not exist on disk, fallback to index.html (SPA routing)
        if not os.path.exists(full_path) or (os.path.isdir(full_path) and not os.path.exists(os.path.join(full_path, "index.html"))):
            self.path = "/index.html"
            
        return super().do_GET()

if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), SPAServerHandler) as httpd:
        print(f"SagarSambandh SPA dev server running at http://localhost:{PORT}/")
        sys.stdout.flush()
        httpd.serve_forever()
