



import tkinter as tk
from tkinter import ttk

choices = ['A','B','C','D','E']

window = tk.Tk()
window.geometry('300x300')
dropdown = ttk.Combobox(window,values=choices)
dropdown.pack()

window.mainloop()






































