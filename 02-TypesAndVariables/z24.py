a=input("Enter vehicle registration number: ")
while a[0:2] == "KK" or a[0:2] == "KR":
    print("Car from Kraków:", True)
    break
else:
    print("Car from Kraków:", False)
    