import investpy


def photo(bot, message, imagename):
    photo = open(imagename, 'rb')
    bot.send_photo(message.chat.id, photo)
    photo.close()