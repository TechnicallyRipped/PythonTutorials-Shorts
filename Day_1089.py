

class NegativeBalance(Exception):
    def __init__(self,bal,wdraw):
        super().__init__(f"Can't withdraw {wdraw} from {bal}")
        self.bal = bal
        self.wdraw = wdraw

balance = 15
withdraw = 100

new_balance = balance - withdraw
if new_balance < 0:
    raise NegativeBalance(balance,withdraw)
balance = new_balance

print(f'Ending balance: {balance}')





