


import fileinput

# for line in fileinput.input(files=['z1.txt', 
#                                    'z2.txt']):

lines = list(fileinput.input(files=['z1.txt',
                                    'z2.txt']))

lines = ''.join(lines)

print(lines)














