file = open("copy.txt", "r", encoding="UTF-8")
for i in file:
    print(i, end="")
file.close()