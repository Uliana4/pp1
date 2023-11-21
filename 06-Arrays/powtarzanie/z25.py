arr=[15, 8, 31, 47, 2, 19]
n = len(arr)
sum=0
i = 0
while i<len(arr):
    sum+=arr[i]
    i+=1
print(*arr)
print(f'The arithmetic mean: {sum/n}', end=" ")