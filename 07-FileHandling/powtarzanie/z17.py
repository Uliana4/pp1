f=open("15.txt", 'r', encoding="UTF-8")
a=f.read()
f.close()

f=open("15.txt", "r", encoding="utf-8")
a=int(len(f.readlines())//5)
f.close()

f=open('15.txt', "r", encoding='UTF-8')
for i in range(a):
    print(f.readline(), end="")
    print(f.readline(), end="")
    print(f.readline(), end="")
    print(f.readline(), end="")
    print(f.readline(), end="")
    a=input()
f.close()