import telebot

bot = telebot.TeleBot('1661693507:AAFMH6FVV5eIazF2mwR6GV6vvBCbkjCkWY0')


def main():
    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        if message.text == "Привет":
            bot.send_message(message.from_user.id, "Привет, я подскажу тебе расписание пар на сегодня.")
        elif message.text == "/help":
            bot.send_message(message.from_user.id, "Напиши Привет")
        else:
            bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

        bot.polling(none_stop=True, interval=0)


if __name__ == '__main__':
    main()
