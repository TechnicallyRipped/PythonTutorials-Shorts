

import pandas as pd

df = pd.read_excel("test.xlsx",
                   sheet_name=None)

for name, ind_df in df.items():
    print(f"Sheet: {name}")
    print(ind_df)












#, sheet_name=None)
# print(all_sheets)
# This returns a dictionary: {sheet_name: DataFrame}
# for name, df in all_sheets.items():
#     print(f"Sheet: {name}")
#     print(df.head())
