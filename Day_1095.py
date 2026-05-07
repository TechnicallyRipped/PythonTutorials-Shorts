

import tkinter as tk
from tkinter import colorchooser

root = tk.Tk()

def pick_color():
    color = colorchooser.askcolor()
    print(color)

tk.Button(root, 
       text="Pick Color", 
       command=pick_color).pack()

root.mainloop()














