


from PIL import Image

image = Image.open('nature.jpg')

image2 = image.convert('L')
image2.show()




# Convert to 1-bit pixels (black and white)
# image_1bit = image.convert('1').show()

# Convert to 8-bit grayscale
# image_grayscale = image.convert('L').show()

# # Convert to 8-bit color using a palette of up to 256 colors
# image_palette = image.convert('P').show()

# # Convert to true color (RGB)
# image_rgb = image.convert('RGB').show()

# # Convert to true color with alpha channel (RGBA)
# image_rgba = image.convert('RGBA').show()

# # Convert to CMYK color space
# image_cmyk = image.convert('CMYK').show()

# # Convert to YCbCr color space
# image_ycbcr = image.convert('YCbCr').show()

# # Convert to LAB color space
# image_lab = image.convert('LAB').show()

# # Convert to HSV color space
# image_hsv = image.convert('HSV').show()

# # Convert to 32-bit signed integer pixels
# image_int = image.convert('I').show()

# # Convert to 32-bit floating point pixels
# image_float = image.convert('F').show()















