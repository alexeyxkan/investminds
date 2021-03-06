import telebot
import config


def get_keyboard(buttons):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    for button in buttons:
        markup.add(telebot.types.KeyboardButton(button))
    return markup


def menu(message, bot):
    markup = get_keyboard(['Избранные корреляции',
                           'Популярные показатели',
                           'Сезонности',
                           'Конуструктор'])
    bot.send_message(message.chat.id, 'Главное меню', reply_markup=markup)


def tools(message, bot):
    markup = get_keyboard(['Корреляции с treasuries', 'Risk on/Risk off',
                           'Схожие активы', 'Другие',
                           'Главное меню'])

    bot.send_message(message.chat.id, 'Выберите тип инструмента',
                     parse_mode='html', reply_markup=markup)


def stocks(message, bot):
    markup = get_keyboard(['Корреляция отношения Финансого сектора ' 
                         + 'к S&P 500 и ставки по 10-летним tresuries',
                           'Корреляция отношения меди ' 
                         + 'к золоту и стаки по 10-летним tresuries'])
    bot.send_message(message.chat.id, 'Меню акций:', reply_markup=markup)