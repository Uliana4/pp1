price=int(input("Enter product price: "))
prod=int(input("Enter number of products purchased: "))
if prod > 2:
    to_pay = (prod-2)*(price - price*0.25) + 2*price
else:
    to_pay = price * prod
print(f"Amount to pay: {to_pay}")