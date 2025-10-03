
import tkinter as tk
from PIL import ImageGrab

def take_screenshot():
    x = root.winfo_rootx()
    y = root.winfo_rooty()
    w = x + root.winfo_width()
    h = y + root.winfo_height()

    screenshot = ImageGrab.grab(bbox=(x, y, w, h))
    screenshot.save("app_screenshot.png")

root = tk.Tk()
root.geometry("300x200")
btn = tk.Button(root, 
                text="Capture Window",
                command=take_screenshot)
btn.pack(pady=20)
root.mainloop()