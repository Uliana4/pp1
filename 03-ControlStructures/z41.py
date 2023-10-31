passw = "0805"

for i in range(1,4):
    a = input("Enter the PIN code: ")
    if a != passw:
        print ("Incorrect...")
    else: 
        print("Correct")
        break
for i in range(3,4):
    if a != passw:
        print("Sorry, your payment card has been blocked.")