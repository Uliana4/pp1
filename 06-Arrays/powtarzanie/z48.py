def create_2d_arr(x,y):
    arr=[]
    for i in range(x):
        row = [0]*y
        arr.append(row)
    return arr
print(create_2d_arr(3,5))