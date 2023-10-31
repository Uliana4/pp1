sum = 0
for i in range(10000):
    a = int(input("Enter number: "))
    sum += a
    if a == 0:
        break
    if i > 0:
        mean = sum / (i+1)
    else:
        mean = 0
print(f'RESULT: Quantity={i}, Sum={sum}, Mean={mean}')