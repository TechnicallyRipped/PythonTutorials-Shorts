






import ctypes

user32 = ctypes.windll.user32
cursor_position = user32.SetCursorPos


cursor_position(600, 200)






















