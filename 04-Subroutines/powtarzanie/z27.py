def f(card_number):
    if len(card_number) == 16:
        return card_number[:2] + 10*"*" + card_number[-4:]
    else:
        print("Enter a 16 digit card number: ")
        
print(f("5290312400019022"))