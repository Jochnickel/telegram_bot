
import threading
import time
from .TeleApi import TeleApi
from .POSTServer import Server


class TeleBot:
	def __init__(self, token: str, webhook: bool = False):
		self.__api = TeleApi(token)

		if webhook:
			self.__poster = Server()
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
