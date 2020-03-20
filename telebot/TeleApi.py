import urllib.request
import requests
import json

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
			print('%ssendMessage?chat_id=%s&text=%s\n'%(self.__preUrl,chat_id,text))
			print(e)
			if   400 == e.code:
				print('User may not exist')
			elif 403 == e.code:
				raise
			elif 404 == e.code:
				print('Token may not be valid')
			else:
				raise
	def sendPoll(
		self,
		chat_id: str or int,
		question: str,
		options: list,
		is_anonymous: bool = True,
		type_: str = 'regular', # regular or quiz
		allows_multiple_answers: bool = False,
		correct_option_id: int = None,
		is_closed: bool = False,
		disable_notification: bool = False,
		reply_to_message_id: int = None,
		reply_markup = None
	):
		if type(chat_id)!=str and type(chat_id)!=int: raise TypeError
		if type(question)!=str: raise TypeError
		if type(options)!=list: raise TypeError
		if len(options)<2: raise ValueError
		if type(is_anonymous)!=bool: raise TypeError
		if type(allows_multiple_answers)!=bool: raise TypeError
		if type(correct_option_id)!=int and None!=correct_option_id: raise TypeError
		if type(is_closed)!=bool: raise TypeError
		if type(disable_notification)!=bool and None!=disable_notification: raise TypeError
		if type(reply_to_message_id)!=int and None!=reply_to_message_id: raise TypeError
		if type(reply_markup)!=None: pass
		
		options = json.dumps(options)

		with requests.post('%ssendPoll?chat_id=%s&question=%s&options=%s'%(self.__preUrl,chat_id,question,options)) as r:
			if not r.ok: print(r.content)
		
	def sendChatAction(
		self,
		chat_id: str or int,
		action: str # typing upload_photo record_video upload_video record_audio upload_audio upload_document find_location record_video_note upload_video_note 
	):
		if type(chat_id)!=str and type(chat_id)!=int: raise TypeError
		if type(action)!=str: raise TypeError

		with requests.post('%ssendChatAction?chat_id=%s&action=%s'%(self.__preUrl,chat_id,action)) as r:
			if not r.ok: print(r.content)

	def sendVenue(
		self,
		chat_id: int or str,
		latitude: float,
		longitude, float,
		title: str,
		address: str,
		foursquare_id: str = None,
		foursquare_type: str = None,
		disable_notification: bool = None,
		reply_to_message_id: int = None,
		reply_markup = None
	):
		with requests.post('%sendVenue?chat_id=%s&latitude=%s&longitude=%s&title=%s&address=%s'%(self.__preUrl,chat_id,latitude,longitude,title,address)) as r:
			if not r.ok: print(r.content)
	# def 
