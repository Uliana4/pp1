f=open("15.txt", "r", encoding="UTF-8")
f1=open("copylines.txt","w", encoding="utf-8")
for line in f:
    f1.write(f'{line}')
f.close()
f1.close()