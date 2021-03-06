import telebot
import config
import markup
import invest
import send


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def command_start(message):
    bot.send_message(message.chat.id, 'Hi!\n'
                                      'Welcome to the Invest minds bot!',
                     parse_mode='html')
    markup.menu(message, bot)


@bot.message_handler(commands=['menu'])
def command_menu(message):
    markup.menu(message, bot)


@bot.message_handler(content_types=['text'])
def chat(message):
    if message.chat.type == 'private':
        if message.text == 'Избранные корреляции':
            markup.tools(message, bot)
        if message.text == 'Популярные показатели':
            markup.tools(message, bot)
        if message.text == 'Сезонности':
            markup.tools(message, bot)
        if message.text == 'Конструктор':
            markup.tools(message, bot)

        elif message.text == 'Корреляции с treasuries':
            markup.stocks(message, bot)
        elif message.text == 'Risk on/Risk off':
            bot.send_message(message.chat.id, 'Облигации:')
        elif message.text == 'Схожие активы':
            bot.send_message(message.chat.id, 'Commodities')
        elif message.text == 'Другие':
            bot.send_message(message.chat.id, 'FX:')

        elif message.text == ('Корреляция отношения Финансого сектора ' + 
                              'к S&P 500 и ставки по 10-летним tresuries'):
            send.photo(bot, message, 'images/correlation_xfl_spx_to_us10yt.png')
        elif message.text == ('Корреляция отношения меди ' + 
                              'к золоту и стаки по 10-летним tresuries'):
            send.photo(bot, message, 'images/correlation_copper_gold_to_us10yt.png')
            
        elif message.text == '/forceupdate':
            invest.update_all()
            invest.watermark_text_all()
            bot.send_message(message.chat.id, 'Updated')
        elif message.text == 'Главное меню':
            markup.menu(message, bot)
        else:
            bot.send_message(message.chat.id, 'Я вас не понимаю.\n Попробуйте еще раз.')


bot.polling(none_stop=True)

