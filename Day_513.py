

from openpyxl import load_workbook

wb = load_workbook('New_tab.xlsx')

sheet1 = wb['tab1']

wb.remove(sheet1)

wb.save('New_tab.xlsx')
