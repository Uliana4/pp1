def f(number1,number2,number3):
    if number1>number2 and number1>number3 and number2>number3:
        l = number1
        s=number3
        d=l-s
    elif number1>number2 and number1>number3 and number3>number2:
        l = number1
        s=number2
        d = l-s
    elif number2>number3 and number2> number1 and number3>number1:
        l= number2
        s=number1
        d =l-s
    elif number2>number3 and number2> number1 and number1>number3:
        l= number2
        s=number3
        d = l-s
    elif number3>number2 and number3>number1 and number2>number1:
        l=number3
        s=number1
        d = l-s
    elif number3>number2 and number3>number1 and number1>number2:
        l=number3
        s=number2 
        d = l-s 
    return d
    

print(f(7,4,9))
print(f(2,12,8))