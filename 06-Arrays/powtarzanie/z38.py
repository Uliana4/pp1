def f(array, number):
    count = 0
    for i in array:
        if i>number:
            count+=1
    return count
        
print(f([1,2,5,6,7,3,8], 3))
