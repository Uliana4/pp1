n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
if n1 > n2:
    print(f'Numbers in ascending order: {n2}, {n1}')
elif n2>n1:
    print(f'Numbers in ascending order: {n1}, {n2}')
else:
     print(f'Numbers in ascending order: {n1}={n2}')