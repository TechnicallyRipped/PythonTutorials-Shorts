



import tkinter as tk
from tkinter import messagebox

app = tk.Tk()

def show_error_message():
    messagebox.showerror("Error", "This is an error message.")

error_button = tk.Button(app, text="Show Error", command=show_error_message)

error_button.pack()

app.mainloop()




























