
import tkinter as tk

def paint(event):
    x,y = event.x,event.y
    canvas.create_rectangle(x, y, x+10, y+10, 
                            fill='black',
                            outline='black')

def clear_canvas(event):
    canvas.delete('all')

window = tk.Tk()

canvas = tk.Canvas(window, bg="white", 
                   width=400, height=400)
canvas.pack()

canvas.bind("<B1-Motion>", paint)
window.bind("<space>", clear_canvas)

window.mainloop()
