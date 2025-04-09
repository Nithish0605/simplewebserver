from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<html>
<head>
<title>Top Software Industries</title>
</head>
<body>
<table border="1" cellspacing="10" cellpadding="6">
<caption>Top 5 Revenue Generating Software Companies</caption>
<tr>
<th>S.no</th>
<th>Companies</th>
<th>Revenue</th>
</tr>
<tr>
<th>1</th>
<th>Microsoft</th>
<th>43 billion</th>
</tr>
<tr>
<th>2</th>
<th>Oracle</th>
<th>29.6 billion</th>
</tr>
<tr>
<th>3</th>
<th>IBM</th>
<th>29.1 billion</th>
</tr>
<tr>
<th>4</th>
<th>SAP</th>
<th>16.8 billion</th>
</tr>
<tr>
<th>5</th>
<th>Symantec</th>
<th>5.6 billion</th>
</tr>
</table>
</body>
</html>
"""

class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())

server_address = ('', 8000)
httpd = HTTPServer(server_address, myHandler)
print("My webserver is running...")
httpd.serve_forever()