def f(arr1, arr2):
    for j in arr1:
        if j in arr2:
            return True
        else: 
            return False
        
print(f([1,2,3],[1,2,3,4,5,6]))
print(f([7,8],[1,2,3,4,5,6]))