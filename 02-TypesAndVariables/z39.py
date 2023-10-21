price = float(input(" Enter price: "))
discount = int(input(" Enter discount %: "))
rd = price * (discount/100)
pd = price - rd
print(f" Price with discount: {pd:.2f} \n Reduction: {rd:.2f}")