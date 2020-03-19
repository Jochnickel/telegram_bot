from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl
import threading

class MyHandler(BaseHTTPRequestHandler):
	def do_POST():
		content_length = int(self.headers['Content-Length'])
		body = self.rfile.read(content_length)
		print(body)


httpd = HTTPServer(('', 80), MyHandler)

threading.Thread(target = httpd.serve_forever).start()
print('Webhook Server running!')




#httpd.socket = ssl.wrap_socket (httpd.socket,
#        keyfile='/etc/letsencrypt/live/bot1.telegram.jj22.de/privkey.pem',
#        certfile='/etc/letsencrypt/live/bot1.telegram.jj22.de/fullchain.pem', server_side=True)

