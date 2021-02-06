import telebot
from telebot import types

# @BtfNeDetBot

bot = telebot.TeleBot("1508006515:AAFRz-eNDwas7qdgDb_k6DQXRNheIHjt06k")

user_data = {}

class User:
    def __init__(self, fname):
        self.fname = fname
        self.lname = ''



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, "Приветики")
    # bot.reply_to(message, "Приветики")
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    question = 'Ты хочешь задать вопрос?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard) \


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, "Приятно познакомиться! Теперь запишу в БД!")
    elif call.data == "no":
        bot.send_message(call.message.chat.id, "Тогда бай бай!")
        # bot.register_next_step_handler(call.message, reg_name))


if __name__ == '__main__':
    bot.polling(none_stop=True)


# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
#     if message.text == 'Привет':
#         bot.reply_to(message, 'Привет создатель бота!')
#     elif message.text == 'hi':
#         bot.reply_to(message, 'Hi again! The bot creator!')
#     elif message.text == '/reg':
#
#         bot.send_message(message.from_user.id, "Привет! Давай познакомимся! Как тебя зовут?")
#         bot.register_next_step_handler(message, reg_name)
#
#
# def reg_name(message):
#     global name
#     name = message.text
#     bot.send_message(message.from_user.id, "Какая у вас фамилия?")
#     bot.register_next_step_handler(message, reg_surname)
#
#
# def reg_surname(message):
#     global surname
#     surname = message.text
#     bot.send_message(message.from_user.id, "Сколько вам лет?")
#     bot.register_next_step_handler(message, reg_age)
#
#
# def reg_age(message):
#     global age
#
#     while age == 0:
#         age = int(message.text)
#
#     if message.text == int:
#         age = message.text
#     else:
#         bot.send_message(message.from_user.id, "Вводите цифрами!")
#     # age = message.text
#     # while age == 0:
#     #     try:
#     #         age = int(message.text)
#     #     except Exception:
#     #         bot.send_message(message.from_user.id, "Вводите цифрами!")
#
#     keyboard = types.InlineKeyboardMarkup()
#     key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
#     keyboard.add(key_yes)
#     key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
#     keyboard.add(key_no)
#     question = 'Тебе ' + str(age) + ' лет? И тебя зовут: ' + name + ' ' + surname + '?'
#     bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
#
# #
# @bot.callback_query_handler(func=lambda call: True)
# def callback_worker(call):
#     if call.data == "yes":
#         bot.send_message(call.message.chat.id, "Приятно познакомиться! Теперь запишу в БД!")
#     elif call.data == "no":
#         bot.send_message(call.message.chat.id, "Попробуем еще раз!")
#         bot.send_message(call.message.chat.id, "Привет! Давай познакомимся! Как тебя зовут?")
#         bot.register_next_step_handler(call.message, reg_name)
#
#
# bot.polling()