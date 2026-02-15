
# Using pandas, write a solution to find the second
# highest salary from the given DF, and return a
# DF with all employees with that salary

import pandas as pd

df = pd.DataFrame({
    "employee": ["Joe","Bob","Chris","Mike","Frank"],
    "salary": [70000, 90000, 90000, 60000, 80000]
})

x = df["salary"].drop_duplicates().nlargest(2).iloc[-1]

result = df[df['salary'] == x]

print(result)


