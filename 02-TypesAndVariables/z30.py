import random
a= int(random.uniform(1, 7))
for a in range(1,7):
    print(f' Dice rolled: {a}')
    if a == 6 or a == 1 :
        print(" Special number: True")
        break
    else:
        print(' Special number: False')