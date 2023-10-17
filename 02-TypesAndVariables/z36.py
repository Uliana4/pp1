buy = float(input("Bank buys EUR: "))
sell = float(input("Bank sells EUR: "))
spread = (buy - sell)

if spread<0:
    spread = round(spread, 4) * (-1)
else:
    spread = round(spread, 4)

print(f'Spread: {spread}')