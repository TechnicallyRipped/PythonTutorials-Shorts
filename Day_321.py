


import multiprocessing
import platform


cpu_count = multiprocessing.cpu_count()
print("CPU Count:", cpu_count)

cpu_name = platform.processor()
print("CPU Name:", cpu_name)












