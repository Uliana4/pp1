arr=[15, 8, 31, 47, 2, 19]
print(*arr)
sum=0
for i in arr:
    sum += i
print(f'srednie to {sum/len(arr)}', end="")