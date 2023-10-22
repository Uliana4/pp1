time24 = input("Enter time (24-hour format \"20:24\") : ") 
b = int(time24[3:])
for i in time24:
    a = int(time24[:2])
    if a in range(1,12):
        a = int(a)
    else:
        a = int(a - 12)
        break
print(f"Time in 12-hour format: {a}:{b}")
