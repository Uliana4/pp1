def f(number):
    sum = 0
    str_number = str(number)
    for i in str_number:
        if str_number.count(i) > 1:
            sum += int(i)
    return sum

print(f(1027))
print(f(230335))
print(f(513553007))