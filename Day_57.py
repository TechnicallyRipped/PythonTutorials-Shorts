
from PIL import Image

image = Image.open('nature.jpg')

horizontal_flip = image.transpose(Image.FLIP_LEFT_RIGHT)

vertical_flip = image.transpose(Image.FLIP_TOP_BOTTOM)

image.show()
horizontal_flip.show()
vertical_flip.show()
































