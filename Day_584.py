


# pip install pyautogui
# pip install keyboard

import pyautogui
import keyboard
import random
import time

while True:
    pyautogui.scroll(random.randint(-500, -200))
    time.sleep(random.random()) 
    if keyboard.is_pressed('r'):
        break
