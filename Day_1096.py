

import tkinter as tk

root = tk.Tk()

x = tk.Button(root, 
              text="Destroy Me", 
              command=lambda: x.destroy())

x.pack(padx=100, pady=100)

root.mainloop()














