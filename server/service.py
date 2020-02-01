import http.server
from urllib.parse import parse_qs
import database
import json
import os

class OERDatabaseHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        self.log_message("path: %s", self.path)
        try:
            resource = self.path
            if '?' in self.path:
                [resource, queryString] = self.path.split('?')
                self.log_message("query string: %s", queryString)
            
            self.log_message("resource: %s", resource)
            if resource == "/add":
                self.process_add(queryString)
            elif resource == '/search':
                self.process_search(queryString)
            elif resource == "/":
                self.process_resource_request('index.html', 'text/html')
            elif resource.endswith('.html'):
                self.process_resource_request(resource[1:], 'text/html')
            elif resource.endswith('.css'):
                self.process_resource_request(resource[1:], 'text/css')
            elif resource.endswith('.png'):
                self.process_resource_request(resource[1:], 'image/png')
            elif resource.endswith('.js'):
                self.process_resource_request(resource[1:], 'text/javascript')
            
        except Exception as e:
            self.send_error(400, str(e))

    # This query will be of the form ?term={}&searchType={title|author|subject|summary}
    def process_search(self, queryString):
        search_terms = parse_qs(queryString)
        self.log_message("search terms... qs = %s", str(search_terms))

        term = search_terms['term'][0]
        search = database.fetch_match(term, search_terms['searchType'][0])

        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(search, 'UTF-8'))

    def process_add(self, queryString):
        add_terms = parse_qs(queryString)
        self.log_message("search terms... qs = %s", str(add_terms))
            
        argument_list = self.get_add_arguments(add_terms)
        database.add_textbook(argument_list)
            
        self.send_response(200)
        self.end_headers()

    def process_resource_request(self, resource, mime):
        with open(resource, 'rb') as f:
            self.send_response(200)
            self.send_header('Content-Type', mime)
            self.end_headers()
            self.wfile.write(f.read())

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
    os.chdir(os.path.join('.', 'app'))
    daemon = http.server.HTTPServer(('', 8000), OERDatabaseHandler)
    daemon.serve_forever()