# import telebot
# import types


# token = '2146925836:AAFFuoenaespbet7MEH24DQYKAPxo4C3YuI'

# bot = telebot.TeleBot(token)

# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id,'Ухадиииииии')


# @bot.message_handler(commands=['button'])
# def button_message(message):
#     markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
#     item1=types.KeyboardButton("Прибухнуть")
#     markup.add(item1)
#     bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)


# @bot.message_handler(content_types='text')
# def message_reply(message):
#     if message.text=="Прибухнуть":
#         bot.send_message(message.chat.id,"https://krasnoeibeloe.ru/")

# # Почему то не работает
# @bot.message_handler(content_types='text')
# def say_lmao(message):
#     if message.text=="Привет":    
#         bot.reply_to(message, "Здорово заебал")

# bot.infinity_polling()