
import pandas as pd

df = pd.DataFrame({
    'Name': ['Joe', 'John', 'Mike'],
    'Math': [88, 92, 85],
    'Science': [91, 87, 93]
})

styled_df = df.style.highlight_max(axis=0,
                                   subset=['Math','Science'],
                                   color='green')
styled_df = styled_df.highlight_min(axis=0,
                                   subset=['Math','Science'],
                                   color='red')

styled_df.to_excel('df_1_style.xlsx',index=False)
