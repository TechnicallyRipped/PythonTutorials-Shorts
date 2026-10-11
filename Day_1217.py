

# pip install Pillow
from PIL import Image

image = Image.open("mb.jpg")
image = image.convert("RGB")
image.save("mb.pdf")