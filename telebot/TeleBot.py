import threading
import time
from .TeleApi import TeleApi
from .Webhook import Webhook
from .NoWebhook import NoWebhook
import urllib.request
import os

REPO = 'https://raw.githubusercontent.com/Jochnickel/telegram_bot/master/telebot/'

class TeleBot:
	def __init__(self, token: str, set_webhook: str = None, auto_update = True):
		self.__api = TeleApi(token)
		
		if auto_update:
			with urllib.request.urlopen('%sTeleBot.py.version'%(REPO)) as v:
				print(v.read())
		
		if set_webhook:
			self.__poster = Webhook(token = token, webhook_url = set_webhook)
			self.__poster.onPost = self.onMessage
		else:
			self.__poster = NoWebhook(token = token)
			self.__poster.onUpdate = self.onMessage
		def thread_f():
			while True:
				print("Bot running")
				time.sleep(25)
		threading.Thread(target = thread_f).start()
		print("\nBot loaded! CTRL+C to terminate.\n")
	
	def sendMessage(self, id, *a):
		self.__api.sendMessage(id, *a)

	def sendPoll(self, id, *a):
		self.__api.sendPoll(id, *a)
	
	def onMessage(self, message):
		self.sendMessage(452549370, str(message))
		print("New Message: ",message)
