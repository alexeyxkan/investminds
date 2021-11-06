import telebot
import markup


menu_markup = markup.get_keyboard(['Главное меню'])


def correlation_xfl_spx_to_us10yt(message, bot):
    photo = open('images/correlation_xfl_spx_to_us10yt.png', 'rb')
    bot.send_photo(message.chat.id, photo,
                   caption='Корреляция отношения Финансого сектора'
                         + 'к S&P 500 и ставки по 10-летним tresuries',
                   markup=menu_markup)