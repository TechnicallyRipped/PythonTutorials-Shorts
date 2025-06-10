

import tkinter as tk

def show_input():
    user_input = text_box.get(index1="1.0",
                              index2="end")
    print(f"{user_input}")

app = tk.Tk()

text_box = tk.Text(app, height=3, width=30)
text_box.pack(pady=10)

button = tk.Button(app, text="Submit", command=show_input)
button.pack()

app.mainloop()
