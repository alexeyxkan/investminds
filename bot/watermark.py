from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def text(image_path, pos):
    text = 't.me/investmindsbot'
    photo = Image.open(image_path)
 
    # make the image editable
    drawing = ImageDraw.Draw(photo)
 
    black = (3, 8, 12)
    font = ImageFont.truetype("fonts/freemono.ttf", 40)
    drawing.text(pos, text, fill=black, font=font)
    photo.save(image_path)
