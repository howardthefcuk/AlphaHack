import telebot
import config
from telebot import types
import collections
import json

bot = telebot.TeleBot(config.token)

with open('count.json') as data_file:    
    countCode = json.load(data_file)

class buddy:
	def __init__(self, botik):
		self.users = collections.defaultdict(int)
		self.bot = botik 
		self.welcomeMess = "Привет. Если мы встретились, значит ты хочешь рассчитать бюджет своей следующей поездки! Расскажи, куда едешь?"
		self.polite = "Хороший выбор!"
		self.getlink = "Вот интерактивная инфографика по этой стране:\n"
		self.next = "Какую-нибудь еще страну хочешь глянуть?"
		self.err = "Боюсь, я не совсем тебя понял. Можешь переформулировать?"
		
	def getState(self, user):
		return self.users[user]


	def lifetime(self, message):
		temp = message.chat.id
		print('Logging. user: ' + str(message.chat.id) + ' state ' + str(self.getState(message.chat.id)))
		if self.users[temp]==0:
			self.users[temp] = self.actionState0(message)
		elif self.users[temp]==1:
			self.users[temp] = self.actionState1(message)

	def actionState0(self, message):
		usid = message.chat.id
		bot.send_message(message.chat.id, self.welcomeMess)
		return 1

	def actionState1(self, message):
		#if "какие" in message.lower():
		#	res = ""
		#	for i in countCode:
		#	bot.send_message(message.chat.id, self.polite)
		for i in countCode:
			if i.lower() in message.text.lower():
				code = countCode[i]
				bot.send_message(message.chat.id, self.polite)
				keyboard = types.InlineKeyboardMarkup()
				url_button = types.InlineKeyboardButton(text="Перейти к инфографике", url="http://127.0.0.1:8050/"+ code)
				keyboard.add(url_button)
				bot.send_message(message.chat.id, self.getlink, reply_markup=keyboard)
				bot.send_message(message.chat.id, self.next)
				return 1
		bot.send_message(message.chat.id, self.err)
		return 1
		

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    puppy.lifetime(message)

if __name__ == '__main__':
	puppy = buddy(bot)
	bot.polling(none_stop=True)
