arr=[15, 8, 31, 47, 2, 19]
print(*arr)
n= len(arr)
sum=0
i=0
while i<n:
    sum+=arr[i]
    i+=1
print(sum/n, end=' ')