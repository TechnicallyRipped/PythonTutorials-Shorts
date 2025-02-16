import pandas as pd

df = pd.read_csv('melt.csv')

print(df)

x = df.melt(id_vars=['Name'],
            value_vars=['Math', 'English', 'History'],
            var_name='Subject',
            value_name='Score')

print(x)

x.to_csv('long_df.csv')
















