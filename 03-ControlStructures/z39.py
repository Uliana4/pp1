a = int(input("Write an a side: "))
b = int(input("Write a b side: "))

for i in range(1,a):
    print("*" * i)
    i+=1
    for j in range(1, b):
        print("*" * j)
        j+=1
    print()