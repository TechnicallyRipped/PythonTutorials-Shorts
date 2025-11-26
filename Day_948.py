
import tkinter as tk
from tkinter import messagebox

def on_closing():
    if messagebox.askokcancel("Quit", 
                              "You Quit?"):
        root.destroy()

root = tk.Tk()
root.geometry("300x100")

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
