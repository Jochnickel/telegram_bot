from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.request
import ssl
import threading
from io import BytesIO

class Webhook:
	def __init__(self, port = 80, token = None, webhook_url = None):
		if None!=webhook_url:	
			if 'http:'==webhook_url[:5]: raise ValueError('Must be https')
		
		class MyHandler(BaseHTTPRequestHandler):
			def do_GET(selfHandler):
				self.send_response(200)
				self.end_headers()
				self.wfile.write(b'Server running')
			def do_POST(selfHandler):
				content_length = int(selfHandler.headers['Content-Length'])
				body = selfHandler.rfile.read(content_length)
				selfHandler.send_response(200)
				selfHandler.end_headers()
				response = BytesIO()
				response.write(b'This is POST request. ')
				response.write(b'Received: ')
				response.write(body)
				selfHandler.wfile.write(response.getvalue())
				self.onPost(body)
				print("asd")
	
	
		threading.Thread(
			target = HTTPServer(('', port), MyHandler).serve_forever
		).start()
		if token and webhook_url:
			urllib.request.urlopen('%s'%(webhook_url))
			urllib.request.urlopen('https://api.telegram.org/bot%s/setWebhook?url='%(token, webhook_url)):
		print('Webhook Server running!')
	
	def onPost(self, txt):
		print('self.onPost: ',txt)

#httpd.socket = ssl.wrap_socket (httpd.socket,
#        keyfile='/etc/letsencrypt/live/bot1.telegram.jj22.de/privkey.pem',
#        certfile='/etc/letsencrypt/live/bot1.telegram.jj22.de/fullchain.pem', server_side=True)

