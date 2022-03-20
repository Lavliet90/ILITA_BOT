import telebot
from ilitaconfig import token_telegram

bot = telebot.TeleBot(token_telegram)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello")


@bot.message_handler(func=lambda m: True)
def test_pinging(message):
    if message.text.lower() == 'бип':
        print("буп прошел успешно")
        bot.send_message(message.chat.id, "буп")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text.lower() == 'соси':
        print(message.from_user.first_name)
        bot.reply_to(message,
                     f'Сам соси {message.from_user.first_name}')  # Только для беседы, в личке не from_user, a chat
    else:
        pass


bot.infinity_polling()
