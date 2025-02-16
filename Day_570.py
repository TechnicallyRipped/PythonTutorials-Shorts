




with open('print.txt','r') as file:
    x = file.read()
    print(x)
    file.seek(0) 
    y = file.read()
    print(y)
