


from PIL import Image

image = Image.open("nature.jpg")

cropped_image = image.crop((50,100,150,200))

cropped_image.show()
cropped_image.save('cropped img.jpg')







































