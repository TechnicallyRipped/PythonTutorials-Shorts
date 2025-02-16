

import tkinter as tk

app = tk.Tk()

spinbox = tk.Spinbox(app, from_=0, to=10)
spinbox.pack()

def print_value():
    print(f"{spinbox.get()}")

button = tk.Button(app, text="Show Value", 
                   command=print_value)
button.pack()

app.mainloop()




























