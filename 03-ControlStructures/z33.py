number = int(input("Enter decimal number: "))
i = number
b = ""
while number>0:
    a = number %2
    b= str(a)+b
    number = number//2

print(f"{i}(10)={b}(2)")
