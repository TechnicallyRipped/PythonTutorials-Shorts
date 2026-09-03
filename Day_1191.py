



class DOUBLE():
    def __init__(self,number):
        self.number = number
    def __call__(self,value):
        print(self.number * value)

x = DOUBLE(2)

x(10)










