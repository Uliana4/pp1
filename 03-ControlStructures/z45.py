for i in range(10000):
    n = int(input("Enter a number grater then 1: "))
    while n>1:
        if n%1==0:
            if n%n==0:
                print(n)
                break
            else:
                print(" ")