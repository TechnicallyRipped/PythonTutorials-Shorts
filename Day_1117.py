
import pandas as pd 

df1 = pd.DataFrame({
    'Age': [25, 35, 40]
})

df2 = pd.DataFrame({
    'Age': [100,90,80,70]
})

df1.update(df2)

print(df1)