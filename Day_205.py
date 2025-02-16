

import tkinter as tk

app = tk.Tk()
app.geometry('300x100')

checkbox_value = tk.IntVar()
checkbox = tk.Checkbutton(app, text="Checkbox", 
                          font=('Arial',16),
                          variable=checkbox_value)
checkbox.pack()

def print_state():
    print("Checkbox state: ", checkbox_value.get())

button = tk.Button(app, text="Print State", 
                   command=print_state)
button.pack()

app.mainloop()





















