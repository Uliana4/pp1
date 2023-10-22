washing_product = input("to clean up \"Jacket\", \"Underwear\", \"Shoes\" : ")
want_rinse = input("Do u want to do an additional rinse? :")
want_spin = input("Do u want to do an additional spin? :")

additional_spin = 9
additional_rinse = 15

total = 0

if washing_product == "Jacket":
    total += 40
elif washing_product == "Underwear":
    total += 70
elif washing_product == "Shoes":
    total += 20
print(f"Total washing time without rinse and spin: {total} minutes")

if (want_rinse == "yes" and want_spin == "no"):
    total += additional_rinse
    print(f"Total washing time with rinse : {total} minutes")
elif (want_spin == "yes" and want_rinse == "no"):
    total += additional_spin
    print(f"Total washing time with spin : {total} minutes")
elif (want_rinse == "yes" and  want_spin =="yes"):
    total += additional_rinse + additional_spin
    print(f"Total washing time : {total} minutes")