

def print_rect(width:int,height:int,char:str):
    # if len(char) != 1:
    #     raise ValueError("Char length must be 1.")
    for i in range(height):
        if i == 0 or i == height - 1:
            print(char*width)
        else:
            print(char+(' '*len(char))*(width-2)+char)

print_rect(10,5,'**')




