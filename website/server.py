from BaseHTTPServer import HTTPServer as hs
from SimpleHTTPServer import SimpleHTTPRequestHandler as shqh

server = hs(('', 80), shqh)
server.serve_forever()