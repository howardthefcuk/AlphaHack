import telebot
import config
from telebot import types
import collections

bot = telebot.TeleBot(config.token)


class buddy:
	def __init__(self, botik):
		self.users = collections.defaultdict(int)
		self.bot = botik 
		self.welcomeMess = "Привет. Если мы встретились, значит ты хочешь рассчитать бюджет своей следующей поездки! Расскажи, куда едешь?"
		self.polite = "О. Прекрасный выбор."
		self.polite2 = "Тоже неплохой выбор."
		self.food1 = "По моей информации в среднем там тратят на еду "
		self.food2 = " евро в день на человека. Примерные минимум и максимум - "
		self.trans1 = "Транспорт - еще "
		self.trans2 = " евро. (мин/макс - "
		self.enter1 = "И развлечения - "
		self.infog = "Вот напоследок инфографика, чтобы нагляднее это все представить."

		
	def getState(self, user):
		return self.users[user]


	def lifetime(self, message):
		temp = message.chat.id
		print('Logging. user: ' + str(message.chat.id) + ' state ' + str(self.getState(message.chat.id)))
		if self.users[temp]==0:
			self.users[temp] = self.actionState0(message)
		elif self.users[temp]==1:
			self.users[temp] = self.actionState1(message)
		elif self.users[temp]==2:
			self.users[temp] = self.actionState2(message)

	def actionState0(self, message):
		usid = message.chat.id
		bot.send_message(message.chat.id, self.welcomeMess)
		return 1

	def actionState1(self, message):
		bot.send_message(message.chat.id, self.polite)
		bot.send_message(message.chat.id, self.food1+"30"+self.food2+"10 и 100.")
		bot.send_message(message.chat.id, self.trans1+"10"+ self.trans2 + "2 и 40)")
		bot.send_message(message.chat.id, self.enter1+"40, но можно как сэкономить (12), так и пошиковать (154)")
		bot.send_message(message.chat.id, self.infog)
		photo = open('zalupaItaly.png', 'rb')
		bot.send_photo(message.chat.id, photo)
		return 2
	
	def actionState2(self, message):
		bot.send_message(message.chat.id, self.polite2)
		bot.send_message(message.chat.id, self.food1+"20"+self.food2+"7 и 234.")
		bot.send_message(message.chat.id, self.trans1+"15"+ self.trans2 + "3 и 34)")
		bot.send_message(message.chat.id, self.enter1+"20, но можно как сэкономить (8), так и пошиковать (90)")
		bot.send_message(message.chat.id, self.infog)
		photo = open('zalupaGermany.png', 'rb')
		bot.send_photo(message.chat.id, photo)
		return 3
		

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    puppy.lifetime(message)

if __name__ == '__main__':
	puppy = buddy(bot)
	bot.polling(none_stop=True)
