

import tkinter as tk

def print_location():
    x = root.winfo_rootx()
    y = root.winfo_rooty()
    print(f'{x=}, {y=}')

root = tk.Tk()
root.geometry("300x200")
btn = tk.Button(root, 
                text="Locate",
                command=print_location)
btn.pack(pady=20)
root.mainloop()
