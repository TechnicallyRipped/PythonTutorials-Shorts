


from PIL import Image

image = Image.open('sample.png')

image = image.convert('RGBA')
image.show()
pixels = list(image.getdata())

new_pixels = []
color_removed = (255,255,255,255) #white

for pixel in pixels:
    if pixel == color_removed:
        new_pixels.append((0, 0, 0, 0))
    else:
        new_pixels.append(pixel)

image.putdata(new_pixels)
image.save('sample2.png')
image.show()




































