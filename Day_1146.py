


import win32api
import win32print

printer_name = win32print.GetDefaultPrinter()
# print(printer_name)

file_ = 'printThis.txt'

win32api.ShellExecute(
    0, 
    "print", 
    file_, 
    f'/d:"{printer_name}"', 
    ".", 
    0
)













