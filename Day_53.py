


from PIL import Image, ImageFilter


image = Image.open('picture.jpg')

image.show()



# image.filter()



print(image.format)   # e.g. JPEG
print(image.size)     # e.g. (640, 480)
print(image.mode)     # e.g. RGB

blurred_image = image.filter(ImageFilter.BLUR)

# show the original and blurred images side by side
blurred_image.show()

























