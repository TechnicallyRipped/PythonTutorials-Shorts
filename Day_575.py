


try: 
    with open('text.txt','x') as file:
        file.write('New text!')
except FileExistsError:
    print('This file already exists dummy')





































