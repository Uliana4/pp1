def f(amount_to_pay):
    a = amount_to_pay//5
    b= amount_to_pay - a*5
    c = b//2
    z = b - c*2
    return a+c+z
print(f(0))