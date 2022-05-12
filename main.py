import os
import telebot
import logging
import psycopg2
from work_with_messages.count_messages import UpdateMessages
from flask import Flask, request

from config import token_telegram, app_url, db_uri
from work_with_messages.replies_to_messages import RepliesToMessages

bot = telebot.TeleBot(token_telegram)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)

db_connection = psycopg2.connect(db_uri, sslmode='require')
db_object = db_connection.cursor()


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)
    UpdateMessages.update_messages_count(message.from_user.id)


@bot.message_handler(commands=['help'])
def help_bot(message):
    bot.reply_to(message, 'Сейчас бот отлавливает все соси и извинения, вскоре добавим и борьбу')
    UpdateMessages.update_messages_count(message.from_user.id)


@bot.message_handler(func=lambda m: True)
def gachi_requests(message):
    '''
    To catch phrases from the chat
    '''
    bot.reply_to(message, RepliesToMessages.sosi(message))

    UpdateMessages.update_messages_count(message.from_user.id)


@server.route('/' + token_telegram, methods=['POST'])
def get_message():
    '''
    to redirect data to the telegram-bot
    '''
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '!', 200


@server.route('/')
def webhook():
    '''
    sends errors to heroku
    '''
    bot.remove_webhook()
    bot.set_webhook(url=app_url)
    return '!', 200


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
