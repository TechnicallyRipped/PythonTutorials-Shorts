

text = '''This is a really long string that
needs to be split into seperate string, each 
ten characters long'''

size = 10
result = [text[i:i+size] for i in range(0,len(text),size)]

print(result)
