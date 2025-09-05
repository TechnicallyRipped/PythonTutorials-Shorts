

# pip install pyinstaller

import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Hello World App")
    root.geometry("300x300")

    label = tk.Label(root, 
                     text="Hello, World!", 
                     font=("Arial", 16))
    label.pack(pady=50)

    root.mainloop()

if __name__ == "__main__":
    main()


# TYPE 'pyinstaller --onefile Day_866.py' to turn this into an '.exe' file

