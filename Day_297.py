




import pyautogui
import time

mouse_position = pyautogui.position()
print(mouse_position)

interval = .5

try:
    while True:
        mouse_position = pyautogui.position()
        print(mouse_position)
        time.sleep(interval)

except KeyboardInterrupt:
    print("End")

















