
import tkinter as tk
from tkinter import filedialog

def open_folder():
    file_path = filedialog.askdirectory()
    if file_path:
        print("File selected:", file_path)

root = tk.Tk()
root.geometry("300x100")

x = tk.Button(root, text="Open File", command=open_folder)
x.pack(pady=30)

root.mainloop()
