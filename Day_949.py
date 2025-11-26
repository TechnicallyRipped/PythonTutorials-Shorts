
import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[("Text files", "*.txt"),
                   ("All files", "*.*")])
    if file_path:
        print("File selected:", file_path)

root = tk.Tk()
root.geometry("300x100")

x = tk.Button(root, text="Open File", command=open_file)
x.pack(pady=30)

root.mainloop()
