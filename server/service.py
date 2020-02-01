import http.server
from urllib.parse import parse_qs
import json


class OERDatabaseHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        self.log_message("path: %s", self.path)
        try:
            [resource, queryString] = self.path.split('?')
            self.log_message("resource: %s", resource)
            self.log_message("query string: %s", queryString)
            
            # This resource is the beginning of the query of the format
            # 127.0.0.1:8000/search
            if resource != "/search":
                self.log_message("resource: " + resource)
                self.send_error(404)
            
            bands = parse_qs(queryString)
            self.log_message("built bands... qs = %s", str(bands))
            
            #bandsList = self.makeBandsList(bands)
            self.log_message("built bandsList...")
            
            #decoded = decodeResistance(bandsList)
            #body = self.buildResponseBody(decoded)
            
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(body, 'UTF-8'))
        except Exception as e:
            self.send_error(400, str(e))


# start the server
if __name__ == '__main__':
    print("OER Database webserver running")
    daemon = http.server.HTTPServer(('', 8000), OERDatabaseHandler)
    daemon.serve_forever()