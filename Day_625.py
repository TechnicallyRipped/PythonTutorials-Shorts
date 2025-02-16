

import pandas as pd

df = pd.DataFrame({'State':['NY','CA','FL'],
                   'Population':[8.25,38.97,22.61]})


with pd.ExcelWriter('Test.xlsx',engine='openpyxl',mode='a') as file:
    df.to_excel(file, sheet_name='Sheet2', index=False)




