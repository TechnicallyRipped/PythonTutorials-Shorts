

symbol = "*"
height = 12

for i in range(height):
    spaces = " " * (height - i)
    char = symbol * (2 * i + 1)
    print(spaces + char)

print(" " * height + "||")
print(" " * height + "||")
