

import atexit

def close_all():
    print("End of script. Closing all files.")

atexit.register(close_all)

print("Opening a file...")

