

import matplotlib.colors as mcolor

rgb = (215, 255, 255)

hex_color = mcolor.rgb2hex([x/255 for x in rgb])

print(hex_color)

rgb2 = mcolor.hex2color(hex_color)
print(rgb2)

rgb2 = tuple(int(x*255) for x in rgb2)

print(rgb2)









