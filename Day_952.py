
import tkinter as tk
from tkinter.filedialog import askopenfilename
import pandas as pd

def open_file():
    file_path = askopenfilename(
        title="Select a file",
        filetypes=[("CSV Files", "*.csv")])
    if file_path:
        df = pd.read_csv(file_path)
        print(df)

root = tk.Tk()
root.geometry("300x100")

x = tk.Button(root, text="Open CSV File", command=open_file)
x.pack(pady=30)

root.mainloop()
