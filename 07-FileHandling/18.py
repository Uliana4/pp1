f= open('GrainsAndBread.txt', 'r')
a=f.read()
f.close()

f1=open('MeatAndFish.txt', 'r')
b=f1.read()
f1.close()

f2 = open("shoppinglist.txt", "w")
f2.write(f'{a}\n{b}')
f2.close