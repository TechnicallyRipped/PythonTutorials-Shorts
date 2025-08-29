
# pip install Pillow

from PIL import Image

i1 = Image.open('c1.png')
i2 = Image.open('c2.png')
i3 = Image.open('c3.png')

i1.save("colors.gif",
        save_all=True,
        append_images=[i2,i3],
        duration=500,
        loop=0)













