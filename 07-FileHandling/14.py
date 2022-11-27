a=input("File name:")
f=open("countries.txt", "r")
licznik=1
for line in f:
    if a == "countries.txt":
     print(f"number of lines:{licznik}", end="")
     licznik+=1
    else:
     print('Error')  

f.close()