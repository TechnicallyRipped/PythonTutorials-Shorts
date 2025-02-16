

# pip install cryptocompare
import cryptocompare

bitcoin_price = cryptocompare.get_price('LTC', currency='USD')

print(bitcoin_price['LTC']['USD'])






















