import os
import telebot
from flask import Flask, request
from ilitaconfig import *

APP_URL = f'https://ilitabot.herokuapp.com//{token_telegram}'
bot = telebot.TeleBot(token_telegram)
server = Flask(__name__)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo(message):
    bot.reply_to(message, message.text)


@server.route('/' + token_telegram, methods=['POST'])
def get_message():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '!', 200


@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    return '!', 200


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
# import os
# import telebot
# import logging
# from ilitaconfig import token_telegram, app_url
# from flask import Flask, request
#
# bot = telebot.TeleBot(token_telegram)
# server = Flask(__name__)
# logger = telebot.logger
# logger.setLevel(logging.DEBUG)
#
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     username = message.from_user.first_name
#     bot.reply_to(message, f"Hello, {username}!")
#
#
# @server.route(f'/{token_telegram}', methods=['POST'])  # перенаправление сообщений сервера фласк к телеграм боту
# def redirect_message():
#     json_string = request.get_data().decode('utg-8')  # получаем данные от сервера в json
#     update = telebot.types.Update.de_json(json_string)
#     bot.process_new_updates([update])  # перенаправляем к боту
#     return '!', 200
#

#
# @bot.message_handler(func=lambda m: True)
# def test_pinging(message):
#     if message.text.lower() == 'бип':
#         print("буп прошел успешно")
#         bot.send_message(message.chat.id, "буп")
#     elif 'соси' in message.text.lower() or 'sosi' in message.text.lower() or \
#             'саси' in message.text.lower() or 'sasi' in message.text.lower():
#         print(message.text.lower())
#         bot.reply_to(message,
#                      f'Сам соси, {message.from_user.first_name}')  # Только для беседы, в личке не from_user, a chat
#     else:
#         pass


# bot.infinity_polling()
# if __name__ == "__main__":
#     bot.remove_webhook()
#     bot.set_webhook(url=app_url)
#     server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
