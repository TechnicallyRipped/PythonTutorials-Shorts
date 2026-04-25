


class NegativeBalance(Exception):
    pass

balance = 10
withdraw = 100

try: 
    new_balance = balance - withdraw
    if new_balance < 0:
        raise NegativeBalance
    balance = new_balance
except NegativeBalance:
    print('Insufficient Funds')

print(f'Ending balance: {balance}')





