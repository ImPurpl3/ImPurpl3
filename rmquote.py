from PIL import Image, ImageDraw, ImageFont
import requests

quoteapi = requests.get("https://zenquotes.io/api/random")

qjson = quoteapi.json()
quote_form = dict(qjson[0])
quote = f'"{quote_form['q']}"'
author = f"{quote_form['a']}"

bgimg = Image.open("bgimg.png")

tl = ImageDraw.Draw(bgimg)
font_pt = 48
openSans = ImageFont.truetype("fonts/OpenSans-Italic.ttf", font_pt)
openSansAuth = ImageFont.truetype("fonts/OpenSans-LightItalic.ttf", 32)

txtlen = tl.textlength(quote, font=openSans)

while txtlen > 1634:
    font_pt -= 4
    openSans = ImageFont.truetype("fonts/OpenSans-Italic.ttf", font_pt)
    txtlen = tl.textlength(quote, font=openSans)

tl.text((836, 90), quote, font=openSans, fill=(255, 216, 255), align="center", anchor="ms")
tl.text((836, 128), author, font=openSansAuth, fill=(255, 216, 255), align="center", anchor="mm")

bgimg.save("quote.png")