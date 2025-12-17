
import tkinter as tk

def on_enter(e):
    btn.config(bg="blue",foreground='red')

def on_leave(e):
    btn.config(bg="lightgray",foreground='black')

root = tk.Tk()

btn = tk.Button(root,
                text="Example Button",
                foreground='black',
                bg="lightgray")

btn.pack(padx=20, pady=20)

btn.bind("<Enter>", on_enter)
btn.bind("<Leave>", on_leave)

root.mainloop()
