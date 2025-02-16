

import pandas as pd

df = pd.read_csv('df.csv')

# print(df)

highest_grades = df.nlargest(3,'Grade')
print(highest_grades)
lowest_grades = df.nsmallest(3,'Grade')
print(lowest_grades)


