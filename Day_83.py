


import os

files = os.listdir()


file_count = 0
python_count = 0

for file in files:
    file_count += 1
    if file.endswith('.py'):
        python_count += 1


print(file_count)
print(python_count)










































