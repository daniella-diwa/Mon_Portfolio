import os
import subprocess
from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/run':
            try:
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()

                # Exécution du script Python
                result = subprocess.getoutput("python script.py")
                self.wfile.write(result.encode())

            except Exception as e:
                self.wfile.write(f"Erreur : {str(e)}".encode())

        else:
            super().do_GET()

# Port dynamique fourni par Render
PORT = int(os.environ.get("PORT", 9000))

# Écouter sur toutes les interfaces
server = HTTPServer(('0.0.0.0', PORT), MyHandler)
print(f"🚀 Serveur lancé sur http://0.0.0.0:{PORT}")

server.serve_forever()
