

from functools import cache
import time

@cache
def wait_(seconds):
    for i in range(seconds):
        print(f'Waiting {i}')
        time.sleep(1)
    print('Done waiting, returning value now')
    return('Complete')

print(wait_(2)) 
print(wait_(2)) 









