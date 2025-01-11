from PIL import Image, ImageDraw
import requests

quote = requests.get("https://zenquotes.io/api/random")

print(quote.json())