f=open("15.txt", 'r', encoding="utf-8")
a=f.read()
f.close

f=open("copy.txt", 'w', encoding='utf-8')
b=f.write(f'{a}')
f.close