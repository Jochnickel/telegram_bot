from telebot.TeleBot import TeleBot

with open('/root/telegram_bot/token.txt','r') as t:
	bot = TeleBot(token = t.read(), webhook = True)

bot.sendMessage(452549370,"hi")
