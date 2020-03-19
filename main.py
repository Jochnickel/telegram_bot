from telebot.TeleBot import TeleBot

bot = TeleBot(token = open('token.txt','r').read(), webhook = True)

# bot.sendMessage(452549370,"hi")
