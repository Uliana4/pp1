bn = input("Enter binary number witfh 4 el: ")

for i in range(0,1):
    b = bn[:1]
    b = int(b) * 1
    a = bn[1:2] 
    a = int(a) * 2
    sum1 = b+ a
for i in range(0,1):
    d= bn[2:3] 
    d = int(d) * 4
    c = bn[3:4] 
    c = int(c) * 8
    sum2 = d + c
sum = sum1 + sum2
print(f"Binary number in decimal notation: {sum}")