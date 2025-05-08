


import os

folder = r'D:\Code\Technically_Ripped\stuff'

for file in os.listdir(folder):
    file_path = os.path.join(folder, file)
    if file.endswith('.txt'):
        os.startfile(file_path)
        print(f"Opened {file}")
    else:
        print(f"Didn't open {file}")



