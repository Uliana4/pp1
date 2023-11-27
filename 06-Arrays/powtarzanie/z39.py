def f(n):
    odn=[]
    evn=[]

    for i in n:
        if i%2==0:
            evn.append(i)
        else:
            odn.append(i)
    return evn+odn
print(f([1,2,3,4,5,6]))