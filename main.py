import telebot
import parse

#parse.get_data('2021-04-12')


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Привет', 'Пока', 'Расписание ВУЗа')
    bot.send_message(message.chat.id, 'Привет!', reply_markup=keyboard)


@bot.message_handler(commands=['test'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='СПбПУ', callback_data=1))
    markup.add(telebot.types.InlineKeyboardButton(text='СПбГУ', callback_data=2))
    markup.add(telebot.types.InlineKeyboardButton(text='ИТМО', callback_data=3))
    bot.send_message(message.chat.id, text="Какой ВУЗ ты выбираешь, чтобы посмотреть распиание?", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Ещё раз привет!')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Пока!')
    elif message.text == 'Расписание ВУЗа':
        bot.send_message(message.chat.id, 'Введите дату в формате YYYY-MM-DD')
        bot.register_next_step_handler(message, print_shedule)
        #start_message(commands=['test'])
def print_shedule(message):
    t = parse.get_data(message.text)
    for x in t:
        bot.send_message(message.chat.id, x[0] + '\nПрепод: '+ x[1]+ '\nМесто  '+x[2])
    bot.register_next_step_handler(message, send_text)
            
        


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за выбор!')
    answer = ''
    if call.data == '1':
        answer = 'Расписание университета СПбПУ!'
    elif call.data == '2':
        answer = 'Расписание университета СПбГУ!'
    elif call.data == '3':
        answer = 'Расписание университета ИТМО!'

    bot.send_message(call.message.chat.id, answer)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)


bot.polling()
