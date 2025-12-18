

import tkinter as tk

def on_double_click(e):
    print('Double click')

root = tk.Tk()

btn = tk.Button(root, 
                text="Double click me")

btn.pack(padx=20, pady=20)

btn.bind("<Double-Button-1>", on_double_click)

root.mainloop()
