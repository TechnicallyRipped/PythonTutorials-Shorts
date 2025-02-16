

import time

def countdown(t:int):
    while t > 0:
        print(f'Time remaining: {t}')
        time.sleep(1)
        t -= 1
    if t == 0:
        print(f'Timer reached 0!')

countdown(5)

















