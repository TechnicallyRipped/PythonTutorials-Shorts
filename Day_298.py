


import os # used for example 1 & 2
from pathlib import Path # used for example 3

file_path1 = "D:/Code/Technically Ripped/tr/x.txt"
file_path2 = "D:/Code/Technically Ripped/tr/x2.txt"
file_path3 = Path("D:/Code/Technically Ripped/tr/x3.txt")

os.remove(file_path1)

os.unlink(file_path2)

Path.unlink(file_path3)
















