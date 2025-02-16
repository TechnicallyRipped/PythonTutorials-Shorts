


import pandas as pd

name_dictionary = {'Name': ['Roy', 'Chris', 'Bob'],
                   'Age': [25, 30, 20],
                   'Height': ["6'2","5'11", "5'9"]}

df = pd.DataFrame(name_dictionary)

df.to_csv('output.csv', index=True)



















































