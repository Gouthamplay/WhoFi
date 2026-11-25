#!/usr/bin/env python3
"""WhoFi local read-only bridge. No router settings are changed."""
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import json

HOST="127.0.0.1"
PORT=8765
ROUTER="http://192.168.1.1/"

class Handler(BaseHTTPRequestHandler):
    def send_json(self, code, data):
        body=json.dumps(data).encode()
        self.send_response(code)
        self.send_header("Content-Type","application/json")
        self.send_header("Access-Control-Allow-Origin","*")
        self.send_header("Access-Control-Allow-Methods","GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers","Content-Type")
        self.send_header("Content-Length",str(len(body)))
        self.end_headers()
        self.wfile.write(body)
    def do_OPTIONS(self):
        self.send_json(204,{})
    def do_GET(self):
        if self.path=="/api/status":
            self.send_json(200,{"bridge":"online","router":"not_checked","gateway":ROUTER})
            return
        if self.path=="/api/router":
            try:
                req=Request(ROUTER,headers={"User-Agent":"WhoFi-local-bridge/1.0"})
                with urlopen(req,timeout=4) as r:
                    data=r.read(500000)
                    self.send_json(200,{"reachable":True,"http_status":r.status,"content_type":r.headers.get("Content-Type"),"bytes_read":len(data),"preview":data[:1200].decode("utf-8","replace")})
            except HTTPError as e:
                self.send_json(200,{"reachable":True,"http_status":e.code,"message":"Router responded with HTTP error (still reachable).","preview":e.read(1200).decode("utf-8","replace")})
            except Exception as e:
                self.send_json(200,{"reachable":False,"error":str(e)})
            return
        self.send_json(404,{"error":"not_found"})
    def log_message(self, fmt,*args):
        print("[WhoFi]",fmt%args)

print("WhoFi Local Bridge (read-only)")
print("Listening at http://127.0.0.1:8765")
print("Keep this terminal open while using WhoFi. Press Ctrl+C to stop.")
HTTPServer((HOST,PORT),Handler).serve_forever()
