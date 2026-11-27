
import pandas as pd

df = pd.DataFrame({
    'Name': ['John', 'Joe', 'Mike'],
    'Score': [85, 45, 92],
    'Bonus': [5, 10, 3]
})

def tot_score(row):
    return row['Score'] + row['Bonus']

df['TotScore'] = df.apply(tot_score, axis=1)

print(df)