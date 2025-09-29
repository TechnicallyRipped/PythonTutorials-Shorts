
# pip install ttkbootstrap

import ttkbootstrap as tb

app = tb.Window(themename="darkly")

btn = tb.Button(app, text="Click Me")
btn.pack(padx=30, pady=30)

app.mainloop()
















