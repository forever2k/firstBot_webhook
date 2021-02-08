import telebot
import os
from flask import Flask, request


TOKEN = '1508006515:AAFRz-eNDwas7qdgDb_k6DQXRNheIHjt06k'
bot = telebot.TeleBot(TOKEN)


server = Flask(__name__)


@bot.message_handler(commands=['start'])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True,False)
    user_markup.row('/start','/info')
    start_text = str('Привет, '+message.from_user.first_name+'!\nЯ бот на Heroku.')
    bot.send_message(message.chat.id, "Вопрос и ответы успешно зарегистрированы. Спасибо!")


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "it works", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://myfirst-bot-webhook3.herokuapp.com/' + TOKEN)
    return "it worksssssssss", 200


if __name__ == '__main__':
    server.debug = True
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))