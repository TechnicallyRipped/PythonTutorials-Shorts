
import pandas as pd

df = pd.DataFrame({
    'Score': [99,95,85,
              96,87,90],
    'Name': ['Joe']*3 + ['Mike']*3,
    'Subject' : ['Math','Science','Art']*2})

print(df)
