from http.server import SimpleHTTPRequestHandler, HTTPServer
import subprocess

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

# Port modifiable si besoin
PORT = 9000

server = HTTPServer(('127.0.0.1', 9000), MyHandler)
print(f"🚀 Serveur lancé sur http://127.0.0.1:9000")

server.serve_forever()