import telebot
import config


def get_keyboard(buttons):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    for button in buttons:
        markup.add(telebot.types.KeyboardButton(button))


def menu(message, bot):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(telebot.types.KeyboardButton('but1'))
    bot.send_message(message.chat.id, 'Главное меню', reply_markup=markup)


def tools(message, bot):
    markup = get_keyboard(['Акции', 'Облигации',
                           'Commodities', 'FX',
                           'Макропоказатели', 'Главное меню'])

    bot.send_message(message.chat.id, 'Выберите тип инструмента',
                     parse_mode='html', reply_markup=markup)


def stocks(message, bot):
    markup = get_keyboard(['Корреляция отношения Финансого сектора' 
                         + 'к S&P 500 и ставки по 10-летним tresuries'])
    bot.send_message(message.chat.id, 'Меню акций:', reply_markup=markup)