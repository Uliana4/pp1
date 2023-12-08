f=open("MeatAndFish.txt", 'r')
a = f.read()
f.close()

f1=open("GrainsAndBread.txt", 'r')
b = f1.read()
f1.close()

f2=open("allproducts.txt", 'w')
f2.write(f'{a}\n{b}')
f2.close()


