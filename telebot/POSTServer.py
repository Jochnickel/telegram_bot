from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl
import threading

class Server:
	def __init__(self, port = 80):
		class MyHandler(BaseHTTPRequestHandler):
			def do_POST(selfHandler):
				content_length = int(selfHandler.headers['Content-Length'])
				body = selfHandler.rfile.read(content_length)
				selfHandler.send_response(200)
				self.onPost(body)
	
	
		threading.Thread(
			target = HTTPServer(('', port), MyHandler).serve_forever
		).start()
		print('Webhook Server running!')
	
	def onPost(self, txt):
		print('self.onPost: ',txt)

#httpd.socket = ssl.wrap_socket (httpd.socket,
#        keyfile='/etc/letsencrypt/live/bot1.telegram.jj22.de/privkey.pem',
#        certfile='/etc/letsencrypt/live/bot1.telegram.jj22.de/fullchain.pem', server_side=True)

