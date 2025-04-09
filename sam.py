from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<!DOCTYPE html>
<html>
    <head>
        <TITLE> Peace  </TITLE>
    </head>
    <body>
        <table border="10" align="center" cellpading="8" bgcolor="orange">
            <tr>
                <th>S.no</th> <th>layer</th> <th>Protocols</th>
            </tr>
            <tr>
                <td>1.</td> <td>Application layer </td> <td>HTTP,FTP,SSH,DNS,Telenet</td>
            </tr>
            <tr>
                <td>2.</td> <td>transport layer </td> <td>TCP&UDP</td>
            </tr>
            <tr>
                <td>3.</td> <td>Internet Layer</td> <td>IPv4/IPv6</td>
            </tr>
            <tr>
                <td>4.</td> <td>Network access layer</td> <td>MAC,Ethernet</td>
            </tr>
        </table>
    </body>
</html>
'''
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()
