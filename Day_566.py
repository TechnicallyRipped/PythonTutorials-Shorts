


# pip install pillow

from PIL import Image

pic = Image.open("grids.png")

width,height = pic.size

print(width,height)