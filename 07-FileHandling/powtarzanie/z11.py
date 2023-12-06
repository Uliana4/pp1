file = open("numbers.txt", "r")
sum = 0
for i in file:
    sum += int(i)
print(f"The sum of the 5 integer numbers in a file = {sum}")
file.close()