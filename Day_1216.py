

import glob
import shutil

folder = r"D:\Code\Technically_Ripped\mess"

for file in glob.glob(folder + r"\*.txt"):
    shutil.move(file, folder + r"\txt_files")

print('DONE!')