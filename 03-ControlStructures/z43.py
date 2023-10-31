a =0
b =1
print(f'{a}\n{b}')
for i in range(2,21):
    c = a + b
    a = b
    b = c
    print(c)