



import tkinter as tk

def on_button_click():
    print('You pressed the button')

window = tk.Tk()
window.geometry('300x300')

button = tk.Button(window, text="Click Me", 
                   command=on_button_click)
button.pack()

window.mainloop()







































