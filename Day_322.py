

from threading import Thread

def print_numbers(start, end):
    for i in range(start, end):
        print(i)
    print('Thread finished')

thread1 = Thread(target=print_numbers, args=(1, 6))
thread2 = Thread(target=print_numbers, args=(6, 11))

thread1.start()
thread2.start()

thread1.join()
thread2.join()











