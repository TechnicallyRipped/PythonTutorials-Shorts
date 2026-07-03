



import win32api

folder = r"D:\Code\Technically_Ripped"

win32api.ShellExecute(
    0,
    "open",
    folder,
    None,
    None,
    1
)