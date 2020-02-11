# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 15:56:22 2020

@author: ll_stsekeid
"""

import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("192.168.2.163", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()