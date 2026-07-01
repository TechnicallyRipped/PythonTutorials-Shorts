



# pip install Pillow
from PIL import Image

img = Image.open("meme.jpg")

new_img = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

new_img.save("x.png")