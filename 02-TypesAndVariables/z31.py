import random
a = int(random.uniform(1,7))
print(a)
b = int(input("Number from dice, 1-6: "))
if b<1 and b>6:
    print("Enter number from 1 to 6: ")
if a == b:
    print("True")
else: 
    print("False")