import random
with open("integers1.txt", 'w') as f:
    for i in range(50):
        a = random.randint(100,999)
        f.write(f'{a}\n')

