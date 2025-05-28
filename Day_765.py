

import tkinter as tk

app = tk.Tk()
app.geometry('300x300')

scale = tk.Scale(app, from_=0, to=100, 
                 orient='vertical',
                 length=150,
                 width=30)

scale.pack(pady=10)

app.mainloop()
