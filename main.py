from PIL import Image, ImageDraw, ImageFont
import os


images = [file for file in os.listdir() if file.endswith(('jpeg', 'png', 'jpg'))]
for image in images:
    img = Image.open(image)
    img = img.resize((1080, 1080))
    img = img.convert("1")
    width, height = img.size

    draw = ImageDraw.Draw(img)
    text = "-m0rtal"

    font = ImageFont.truetype('arial.ttf', 50)
    textwidth, textheight = draw.textsize(text, font)

    margin = 5
    x = width - textwidth - margin
    y = height - textheight - margin

    draw.text((x, y), text, font=font)

    img.save(image)