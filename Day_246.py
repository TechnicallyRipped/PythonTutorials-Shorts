



import pandas as pd

name = ['John', 'Kyle', 'Brian']
last_name = ['Smith', 'Young', 'Mino']
age = [24,26,23]

df_dict = {'Name' : name,
           'Last Name': last_name,
           'Age' : age}

df = pd.DataFrame(df_dict)

print(df)























