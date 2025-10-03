
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")

button1 = tk.Button(tab1, text="This is Tab 1")
button1.pack(pady=20)

label2 = tk.Label(tab2, text="This is Tab 2")
label2.pack(pady=20)

root.mainloop()
