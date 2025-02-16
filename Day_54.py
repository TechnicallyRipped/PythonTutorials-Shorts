



from PIL import Image, ImageFilter

original_image = Image.open('nature.jpg')

blurred = original_image.filter(ImageFilter.BLUR)


# original_image.show()
# blurred.show()

blurred.save('blurred_nature.jpg')




































