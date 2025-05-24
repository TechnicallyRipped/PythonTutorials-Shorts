

# pip install customtkinter

import customtkinter as ctk
# import tkinter as tk

app = ctk.CTk()
# app = tk.Tk()
app.geometry('300x200')

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

button = ctk.CTkButton(app,text='Click Me')
# button = tk.Button(app,text='Click Me')
button.pack(pady=50)

app.mainloop()












# 

# ctk.set_appearance_mode("dark")
# # ctk.set_default_color_theme("blue")

# app = ctk.CTk()
# app.geometry('300x200')

# button = ctk.CTkButton(app,text='Click Me')
# button.pack(pady=20)

# app.mainloop()