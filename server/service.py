import http.server
from urllib.parse import parse_qs
import database
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
            if resource != "/add":
                self.log_message("resource: " + resource)
                self.send_error(404)
            
            add_terms = parse_qs(queryString)
            self.log_message("search terms... qs = %s", str(add_terms))
            
            argument_list = self.get_add_arguments(add_terms)
            database.add_textbook(argument_list)
            
            body = self.build_valid_addition_body()
            
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(body, 'UTF-8'))
        except Exception as e:
            self.send_error(400, str(e))


    def get_add_arguments(self, qs):
        args = []
        args.append(qs['title'][0])
        args.append(qs['author'][0])
        args.append(qs['subject'][0])
        args.append(qs['summary'][0])
        args.append(qs['link'][0])
        return args

    def build_valid_addition_body(self):
        return '''
               <html lang="en">
               <head>
                 <meta charset="utf-8">
                 <title>BookBank</title>
               </head>
               <body>
                 <h1>Successful Addition was made to the database.</h1>
               </body>
               </html>
               '''

# start the server
if __name__ == '__main__':
    print("OER Database webserver running")
    daemon = http.server.HTTPServer(('', 8000), OERDatabaseHandler)
    daemon.serve_forever()