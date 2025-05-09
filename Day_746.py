


import os

folder = r'D:\Code\Technically_Ripped\stuff'

for i,file in enumerate(os.listdir(folder)):
    file_path = os.path.join(folder, file)
    if file.endswith('.txt'):
        new_name = f'my_file_{i}.txt'
        new_path = os.path.join(folder,new_name)
        os.rename(file_path,new_path)



