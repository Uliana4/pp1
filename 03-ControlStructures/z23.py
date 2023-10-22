age= int(input("Enter the dog age in human ages: "))

if age<=2:
    years=int(age*10.5)
else:
    years=int((age-2)*4 + 2*10.5)
print(f"The dog's age in dog’s years is {years}")