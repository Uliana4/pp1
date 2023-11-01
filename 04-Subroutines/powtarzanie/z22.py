def month(n):
    if n == 1:
        return f"The name of the {n} month is January"
    elif n == 2:
        return f"The name of the {n} month is February"
    elif n == 3:
        return f"The name of the {n} month is March"
    elif n == 4:
        return f"The name of the {n} month is April"
    elif n == 5:
        return f"The name of the {n} month is May"
    elif n == 6:
        return f"The name of the {n} month is June"
    elif n == 7:
        return f"The name of the {n} month is July"
    elif n == 8:
        return f"The name of the {n} month is August"
    elif n == 9:
        return f"The name of the {n} month is September"
    elif n == 10:
        return f"The name of the {n} month is October"
    elif n == 11:
        return f"The name of the {n} month is November"
    elif n == 12:
        return f"The name of the {n} month is December"

print(month(n=int(input("Enter month number: "))))

# def month(n): 
#    a = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
#    return (f"The name of month {n} is {a[n-1]}")

# print(month(6))