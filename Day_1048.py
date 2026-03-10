

import pandas as pd

df = pd.DataFrame({
    'name': ['John', 'Mike', 'John', 
             'Alex', 'Mike', 'John']
})

x = df['name'].value_counts().idxmin()

print(x)
