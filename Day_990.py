

from pathlib import Path

folder = Path("D:/pathlibEx")

files = list(folder.iterdir())

for file in files:
    if file.is_file():
        print(f'{file} is a file!')
    elif file.is_dir():
        print(f'{file} is a folder!')