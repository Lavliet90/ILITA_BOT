import os
import telebot
import logging
from flask import Flask, request
from ilitaconfig import token_telegram, app_url

bot = telebot.TeleBot(token_telegram)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)



@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)

@bot.message_handler(commands=['help'])
def help_bot(message):
    bot.reply_to(message, 'Сейчас бот отлавливает все соси и извинения, вскоре добавим и борьбу')




@bot.message_handler(func=lambda m: True)
def gachi_requests(message):
    if message.text.lower() == 'бип':
        print("буп прошел успешно")
        bot.send_message(message.chat.id, "буп")
    elif 'соси' in message.text.lower() or 'sosi' in message.text.lower() or \
            'саси' in message.text.lower() or 'sasi' in message.text.lower():
        bot.reply_to(message, f'Сам соси, {message.from_user.first_name}')
        # Только для беседы, в личке не from_user, a chat
    elif 'извини' in message.text.lower() or 'sorry' in message.text.lower() \
            or 'прости' in message.text.lower() or 'прошу прощения' in message.text.lower():
        bot.reply_to(message, f'Sorry for what, {message.from_user.first_name}?')
    else:
        pass


@server.route('/' + token_telegram, methods=['POST'])
def get_message():  #для переправочки данных в тгбота
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '!', 200


@server.route('/')
def webhook():  #высылает ошибки на хероку
    bot.remove_webhook()
    bot.set_webhook(url=app_url)
    return '!', 200


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
