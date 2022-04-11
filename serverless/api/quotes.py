from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import random
from urllib import parse


with open('serverless/data.json') as f:
    data = json.load(f)


def get_random_number():
    n = random.randint(0, len(data))
    return n


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        path = self.path
        url_component = parse.urlsplit(path)
        query_string_list = parse.parse_qsl(url_component.query)
        dic = dict(query_string_list)

        output = '<html><body>'
        output += '<h1>Your Quotes</h1>'
        try:
            q_num = int(dic.get('q_num'))
            for _ in range(q_num):
                quote = data[get_random_number()]['text']
                output += f'<p>{quote}</p>'
            self.wfile.write(output.encode())

        except:
            quote = data[get_random_number()]['text']
            output += f'<p>{quote}</p>'
            self.wfile.write(output.encode())
        output += '</body></html>'
        return


def main():
    # main
    port = 8000
    server_address = ('localhost', port)
    server = HTTPServer(server_address, handler)
    print(f'Server running on PORT: {port}'.format(port))
    server.serve_forever()


if __name__ == "__main__":
    main()
