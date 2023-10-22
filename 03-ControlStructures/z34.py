amount = int(input("Enter the amount in PLN: "))

a = amount//5
b = amount - a*5
c = b//2
z = b - c*2

print(f"The amount of PLN {amount} in coins:", f"5 zl - {a}", f"2 zl - {c}", f"1 zl - {z}", sep = "\n")