def compare(array1, array2):
    if array1==array2:
        True
        return (f'Array1: {array1}\nArray2: {array2}\nComparison: arrays are the same')
    else:
        return False
print(compare(["water","book","sky"],["water","book","sky"]))
print(compare([True,False], [True,False,True]))
print(compare([5,3,1], [5,3,1]))