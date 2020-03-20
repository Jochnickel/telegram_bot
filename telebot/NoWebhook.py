import threading
import requests
import time
import json

class NoWebhook:
	__interval = 2
	__offset = 0
	def __init__(self, token: str):
		requests.get('https://api.telegram.org/bot%s/setWebhook?url='%token)
		def asd():
			while True:
				t = requests.get('https://api.telegram.org/bot%s/getUpdates?offset=%s'%(token,self.__offset)).json()
				if t['result']:
					r = t['result']
					for u in r:
						self.__offset = u['update_id']+1
						self.onUpdate(u)
				time.sleep(self.__interval)
		threading.Thread(
			target = asd
		).start()
		print("noWebook running")
	def onUpdate(self, update):
		print(update)