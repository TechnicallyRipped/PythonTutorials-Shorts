

from zipfile import ZipFile

files = ['df_1.csv','df_2.csv','icon.png']

with ZipFile('zfiles.zip','w') as zipf:
    for file in files:
        zipf.write(file)
        print(f'Added {file} to zip')


















