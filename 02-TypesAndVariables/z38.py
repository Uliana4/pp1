telephone = input("Enter the tel number (9 el): ")
for i in range (0,3):
    i = telephone[:3] + "-"
for a in range(3,6):
    a = telephone[3:6] + "-"
for c in range(6,9):
    c = telephone[6:]
print(f"Telephone number: {i + a + c}")