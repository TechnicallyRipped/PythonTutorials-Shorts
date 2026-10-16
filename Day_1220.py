


class Machine():
    def __init__(self,power):
        self.power = power

    def do_something(self,pCost):
        self.power -= pCost
        print(f'{self.power} remaining')

