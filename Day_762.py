

import tkinter as tk

def paint(event):
    x,y = event.x,event.y
    canvas.create_rectangle(x,y,x+20,y+20,fill="black")

window = tk.Tk()

canvas = tk.Canvas(window, bg="white", 
                   width=400, height=400)
canvas.pack()

canvas.bind("<B1-Motion>", paint)

window.mainloop()
