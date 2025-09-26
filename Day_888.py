
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('300x150')

options = ["A", "B", "C"]

def show_selection():
    print("Selected:", combo.get())

combo = ttk.Combobox(root, 
                     values=options,
                     state='readonly')
combo.pack(pady=20)

btn = tk.Button(root, text="Get Value", command=show_selection)
btn.pack()

root.mainloop()
























