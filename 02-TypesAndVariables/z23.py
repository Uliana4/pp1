a=int(input("Side 1: "))
b=int(input("Side 2: "))
s=int(input("Side 3: "))
p = (a+b+s)/3
k=int((p*(p-a)*(p-b)*(p-s))**0.5)
c=(a*b+b*s+s*a)
print(f' Triangle area: {k} \n Triangle circumference: {c}')