
import tkinter as tk
from tkinter.filedialog import askopenfilenames

def open_folder():
    file_path = askopenfilenames(
        title="Select a file",
        filetypes=[("Text files", "*.txt")])
    if file_path:
        print("File selected:", file_path)

root = tk.Tk()
root.geometry("300x100")

x = tk.Button(root, text="Open File", command=open_folder)
x.pack(pady=30)

root.mainloop()
