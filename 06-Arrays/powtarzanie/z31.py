arr=[2,3,2,5,8,1,9,8]
for i in arr:
    a=[]
    if arr.count(i)>1:
        a.append(i)
   
print(f'Unique elements: {a}')