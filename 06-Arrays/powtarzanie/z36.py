def f(tuple, number):
    for number in tuple:
        a=tuple.count(number)
    return a
print(f((50,20,40,50,30,50),50))