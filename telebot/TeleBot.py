import threading
import time
from .TeleApi import TeleApi
from .Webhook import Webhook
import urllib

REPO = 'https://raw.githubusercontent.com/Jochnickel/telegram_bot/master/telebot/'

class TeleBot:
	def __init__(self, token: str, webhook: bool = False, auto_update = True):
		self.__api = TeleApi(token)
		
		if auto_update:
			with urllib.urlopen('%sTeleBot.py.version'%(REPO)) as v:
				print(v.read())
		
		if webhook:
			self.__poster = Webhook(token = token)
			self.__poster.onPost = self.onMessage
	
		def thread_f():
			while True:
				print("Bot running")
				time.sleep(10)
		threading.Thread(target = thread_f).start()
		print("\nBot loaded! CTRL+C to terminate.\n")
	
	def sendMessage(self, id, text):
		self.__api.sendMessage(id, text)
	
	def onMessage(self, message):
		self.sendMessage(452549370, str(message))
		print("New Message: ",message)
