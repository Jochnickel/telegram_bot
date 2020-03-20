from telebot.TeleBot import TeleBot
import json

with open('token.txt','r') as t:
	# bot = TeleBot(token = t.read(), set_webhook = 'bot1.telegram.jj22.de')
	bot = TeleBot(token = t.read(),)

bot.sendPoll(452549370,"hi",['asd',"ok"])
# print(len([1]))