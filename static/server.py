#!/usr/bin/env python3

#From https://gist.github.com/HaiyangXu/ec88cbdce3cdbac7b8d5
import http.server
import socketserver

PORT = 9003
#DIRECTORY = "/static"
#DIRECTORY = "./"

class HttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {
        '': 'application/octet-stream',
        '.manifest': 'text/cache-manifest',
        '.html': 'text/html',
        '.png': 'image/png',
        '.jpg': 'image/jpg',
        '.svg':	'image/svg+xml',
        '.css':	'text/css',
        '.js':'application/x-javascript',
        '.map':'application/json',
        '.wasm': 'application/wasm',
        '.json': 'application/json',
        '.xml': 'application/xml',
    }
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, directory=DIRECTORY, **kwargs)
    

#httpd = socketserver.TCPServer(("localhost", PORT), HttpRequestHandler)
socketserver.TCPServer.allow_reuse_address = True
try:
    with socketserver.TCPServer(("", PORT), HttpRequestHandler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()
except KeyboardInterrupt:
    pass