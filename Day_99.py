


import tabula
import pandas as pd

pdf_path = "test_chart.pdf"
page_num = 1
dfs = tabula.read_pdf(pdf_path, pages=page_num, multiple_tables=True)

chart = 1
for df in dfs:
    df = pd.DataFrame(df)
    df.to_csv(f't_chart{chart}.csv')
    chart += 1





























