import telebot
from telebot import types

client = telebot.TeleBot("2115999319:AAE_mo_iGxjj-MZqjgMOukMp2Z8prkAHuvw")

@client.message_handler(commands=['start', 'help'])
def send_welcome(message):
	client.send_message(message.chat.id, 'Напишите "Жижа" что бы получить инфу о всех жижек')
	
@client.message_handler(content_types = ["text"])
def jijs(message):
	jijas = ["жижа", "жижи", "жижки", "жиж"]
	if message.text.lower() in jijas:
		mrk = types.InlineKeyboardMarkup()
		btn_caramel = types.InlineKeyboardButton(text = "Карамель", callback_data = "caramel")
		btn_vishnya = types.InlineKeyboardButton(text = "Вишня", callback_data = "vishnya")
		btn_multifruit = types.InlineKeyboardButton(text = "Мультифрукт", callback_data = "multifruit")
		btn_chernika = types.InlineKeyboardButton(text = "Черника", callback_data = "chernika")
		mrk.add(btn_caramel, btn_vishnya, btn_multifruit, btn_chernika)
		client.send_message(message.chat.id, "Вот жижки", reply_markup = mrk)

client.infinity_polling()