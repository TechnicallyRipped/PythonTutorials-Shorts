

import tkinter as tk

def on_triple_click(e):
    print('Triple click')

root = tk.Tk()

b = tk.Button(root, 
                text="Triple click me")

b.pack(padx=20, pady=20)

b.bind("<Triple-Button-1>", on_triple_click)

root.mainloop()
