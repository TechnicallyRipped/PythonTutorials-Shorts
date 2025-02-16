

import pandas as pd

df = pd.read_csv('df_cut.csv')

my_bin = [0,12,19,35,60,100]
my_labels = ['Child', 'Teen', 'Young Adult', 'Adult', 'Senior']

df['Age_Group'] = pd.cut(df['Age'],
                         bins=my_bin,
                         labels=my_labels)

print(df)