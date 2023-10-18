name1 = input("Enter the first person name:")
age1 = int(input("Enter the first person age:"))
name2 = input("Enter the second person name:")
age2 = int(input("Enter the second person age:"))
if age1>=18 and age2>=18:
    print(f"Both {name1} and {name2} are adults")
elif age1>=18 and age2<18:
    print(f"{name1} is an audult, {name2} isn't an  audult")
elif age1<18 and age2>=18:
    print(f"{name1} isn't an audult, {name2} is an  audult")
else:
    print(f"{name1} and {name2} isn't an  audults")