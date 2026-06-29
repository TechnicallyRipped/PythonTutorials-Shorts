

# pip install Pillow
from PIL import Image, ImageDraw, ImageFont

img = Image.open("temp.jpg")

draw = ImageDraw.Draw(img)
font_ = ImageFont.truetype("times",30)

draw.text((385, 150),
          "Learn Python from AI",
          fill="Black",
          font=font_)

draw.text((385, 525),
          "Watch TechnicallyRipped",
          fill="Black",
          font=font_)

img.save("meme.jpg")