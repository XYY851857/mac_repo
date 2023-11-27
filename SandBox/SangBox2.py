price = 18
value = 2000
rate = 0.003
day = 1
fee = 0.2

refund = (price * value * rate * (day / 365))*(1-fee)
print(refund)