

import tkinter as tk
import tkinter.font as tkFont

root = tk.Tk()
root.title("tkFont Example")
root.geometry("300x150")

my_font = tkFont.Font(family="Helvetica", size=16, 
                      weight="bold", slant="italic")

label = tk.Label(root, text="No style")
label.pack(pady=5)
label2 = tk.Label(root, text="Has style!", font=my_font)
label2.pack(pady=5)

root.mainloop()
