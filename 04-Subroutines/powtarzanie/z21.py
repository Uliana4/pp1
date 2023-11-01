import random
def generate_number():
    x = random.randint(1, 9)
    print(x)
    b = int(input("Enter the number from 1 to 9: "))
    if x == b:
        return("You won!")
    else:
        return ("Hahahah")

print(generate_number())