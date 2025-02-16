


# pip install keyboard
import keyboard

def get_any_key():
    for key in range(1,255):
        if keyboard.is_pressed(key):
            return True
    else:
        return False

pressed = False
print('Loop started')
while not pressed:
    pressed = get_any_key()
print('Loop ended')
















