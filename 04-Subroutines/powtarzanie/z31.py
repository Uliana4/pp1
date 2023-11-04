def f(x,y):
    s = 0
    for i in range(x,y+1):
        while i<0:
            if i%2==0:
                s+=1
                i+=1
            else:
                i+=1
                continue
        return s
       

print(f(-7,8))
print(f(-1, 11))