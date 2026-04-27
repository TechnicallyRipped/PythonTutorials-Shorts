

class NegativeBalance(Exception):
    def __init__(self,bal,wdraw):
        self.bal = bal
        self.wdraw = wdraw

balance = 10
withdraw = 100

try: 
    new_balance = balance - withdraw
    if new_balance < 0:
        raise NegativeBalance(balance,withdraw)
    balance = new_balance
except NegativeBalance as e:
    print(f"Can't withdraw {e.wdraw} from {e.bal}")

print(f'Ending balance: {balance}')





