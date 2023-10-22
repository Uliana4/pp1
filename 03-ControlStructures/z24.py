cur=int(input("Enter the product current price: "))
pr=int(input("Enter the product last price: "))
cena= 100-(cur*100/pr)
if cena>=10:
    print(f"Buy the product!!\nProduct price reduced by {int(cena)}%")
else:
    print("No need")