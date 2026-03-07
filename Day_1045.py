

import seaborn as sns

df_names = sns.get_dataset_names()

for name in df_names:
    print(name)

df = sns.load_dataset('dowjones')
print(type(df))
print(df)








# df = sns.load_dataset('penguins')
# print(df)