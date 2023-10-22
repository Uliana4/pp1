num = input("Enter EAN-13 article number: ")
while len(num) == 13:
    print("Article number is correct")
    if num.startswith("590"):
        print("Article manufactured in Poland")
        break
    else:
        print("not from Poland")
else:
    print("Enter 13 elements!!!")