def number(x, y):
    n = int(input("Enter a number: "))
    if n in range(x,y):
        return "yes"
    else:
        return "no"

print(number(5,6))