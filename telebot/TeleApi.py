import urllib.request

API_URL = 'https://api.telegram.org/'

class TeleApi:
	def __init__(self, token: str):
		self.__token = token
		self.__preUrl = '%sbot%s/'%(API_URL,token)

	def sendMessage(
		self,
		chat_id: str or int,
		text: str,
		parse_mode: str = "",
		disable_web_page_preview: bool = False,
		disable_notification: bool = False,
		reply_to_message_id: int = -1,
		reply_markup = None
	):
		if type(chat_id)!=str and type(chat_id)!=int: raise TypeError
		if type(text)!=str: raise TypeError
		if type(parse_mode)!=str: raise TypeError
		if type(disable_web_page_preview)!=bool: raise TypeError
		if type(disable_notification)!=bool: raise TypeError
		if type(reply_to_message_id)!=int: raise TypeError
		if type(reply_markup)!=None: pass
		
		text = urllib.parse.quote(text)


		try: urllib.request.urlopen('%ssendMessage?chat_id=%s&text=%s'%(self.__preUrl,chat_id,text))
		except TypeError: pass
		except urllib.error.HTTPError as e:
			print('%ssendMessage?chat_id=%s&text=%s'%(self.__preUrl,chat_id,text))
			print(e)
			if   400 == e.code:
				print('User may not exist')
			elif 403 == e.code:
				raise
			elif 404 == e.code:
				print('Token may not be valid')
			else:
				raise
