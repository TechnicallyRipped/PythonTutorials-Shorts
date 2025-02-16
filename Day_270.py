


# pip install openpyxl
import openpyxl as xl

workbook = xl.load_workbook('Example.xlsx')
ws = workbook['Ages']

for row in ws.iter_rows(values_only=True,
                        min_row=2):
    print(row)













