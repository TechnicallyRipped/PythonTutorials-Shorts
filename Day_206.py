

import tkinter as tk

app = tk.Tk()
_font = ('Arial',14)

selected_choice = tk.StringVar()

radio_button1 = tk.Radiobutton(app, text="Option 1", 
                               variable=selected_choice, 
                               value="Option 1", 
                               font=_font)
radio_button2 = tk.Radiobutton(app, text="Option 2", 
                               variable=selected_choice, 
                               value="Option 2",
                               font=_font)
radio_button3 = tk.Radiobutton(app, text="Option 3",
                               variable=selected_choice,
                               value="Option 3",
                               font=_font)

radio_button1.pack()
radio_button2.pack()
radio_button3.pack()

app.mainloop()




























