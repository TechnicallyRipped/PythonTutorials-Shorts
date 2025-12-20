
import tkinter as tk

def on_right_click(e):
    b.config(relief="sunken")
    print("Right click detected")

def on_right_release(e):
    b.config(relief="raised")
    print("Right button released")

root = tk.Tk()

b = tk.Button(root, text="Right-click me")
b.pack(padx=20, pady=20)

b.bind("<Button-3>", on_right_click)
b.bind("<ButtonRelease-3>", on_right_release)

root.mainloop()











