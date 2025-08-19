
# pip install rembg
# pip install pillow

from rembg import remove
from PIL import Image

og_img = "og_img.jpg"
removed_bg = "output.png"

inp = Image.open(og_img)
out = remove(inp)
out.save(removed_bg)
