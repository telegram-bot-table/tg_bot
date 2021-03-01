import telebot

bot = telebot.TeleBot('1661693507:AAECqTR1YL52oEbopZiXRunrZs-qJBqKeys')

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/stop', '/help')
    user_markup.row('Поиск', 'Обо мне')
    bot.send_message(message.from_user.id, 'Добро пожаловать!', reply_markup=user_markup)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == "Привет" or message.text == "привет":
        bot.send_message(message.from_user.id, "Привет, я подскажу тебе расписание пар.")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши 'привет'")
    elif message.text == "Обо мне":
        bot.send_message(message.from_user.id, "Я бот, который подскажет тебе расписание занятий на ближайшее время.")
    elif message.text == "Поиск":
        bot.send_message(message.from_user.id, "Скоро здесь появится нужная тебе информация.")
    elif message.text == "/stop":
        hide_markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'Еще увидимся!', reply_markup=hide_markup)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling()