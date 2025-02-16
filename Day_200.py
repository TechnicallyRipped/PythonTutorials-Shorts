

import tkinter as tk

def button_click():
    print("Button Clicked")

root = tk.Tk()


button = tk.Button(root, text="Custom Button", 
                   command=button_click,
                   font=("Arial", 12), 
                   foreground="white", 
                   background="blue", 
                   relief="raised", 
                   width=15,
                   height=3) 

button.pack(padx=20, pady=10)

root.mainloop()





























