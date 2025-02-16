



import tkinter as tk
from tkinter import PhotoImage

app = tk.Tk()

image_file = PhotoImage(file="icon.png")
image_file = image_file.subsample(3,3)
image = tk.Label(app, image=image_file)
image.pack()

app.mainloop()



























