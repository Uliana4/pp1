crcn = input("Enter the credit card number (16 el): ")
for i in range (0,4):
    i = crcn[:4] + " "
for a in range(4,8):
    a = crcn[4:8] + " "
for c in range(8,12):
    c = crcn[8:12] + " "
for s in range(12,16):
    s = crcn[12:]
print(f"Credit card number: {i + a + c + s}")