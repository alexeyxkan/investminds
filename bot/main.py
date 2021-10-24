import telebot
import config


bot = telebot.TeleBot(config.TOKEN)


def show_menu(message):
    # Keyboard
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton('Акции')
    item2 = telebot.types.KeyboardButton('Облигации')
    item3 = telebot.types.KeyboardButton('Commodities')
    item4 = telebot.types.KeyboardButton('FX')
    item5 = telebot.types.KeyboardButton('Макропоказатели')
    item6 = telebot.types.KeyboardButton('Меню')
    markup.add(item1, item2, item3, item4, item5, item6)

    bot.send_message(message.chat.id, 'Главное меню:',
                     parse_mode='html', reply_markup=markup)


def stocks(msg):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton('XFL,SPX,US10YT')
    markup.add(item1)
    bot.send_message(msg.chat.id, 'Меню акций:', reply_markup=markup)


@bot.message_handler(commands=['start'])
def command_start(message):
    bot.send_message(message.chat.id, 'Hi!\n'
                                      'Welcome to the Invest minds bot!',
                     parse_mode='html')

    show_menu(message)


@bot.message_handler(commands=['menu'])
def command_menu(message):
    show_menu(message)


@bot.message_handler(content_types=['text'])
def chat(msg):
    if msg.chat.type == 'private':
        if msg.text == 'Акции':
            stocks(msg)
        elif msg.text == 'Облигации':
            bot.send_message(msg.chat.id, 'Облигации:')
        elif msg.text == 'Commodities':
            bot.send_message(msg.chat.id, 'Commodities')
        elif msg.text == 'FX':
            bot.send_message(msg.chat.id, 'FX:')
        elif msg.text == 'Макропоказатели':
            bot.send_message(msg.chat.id, 'Макропоказатели:')
        elif msg.text == 'XFL,SPX,US10YT':
            bot.send_message(msg.chat.id, 'XFL,SPX,US10YT:')
        elif msg.text == 'Меню':
            show_menu(msg)
        else:
            bot.send_message(msg.chat.id, 'Я вас не понимаю.\n Попробуйте еще раз.')


bot.polling(none_stop=True)

