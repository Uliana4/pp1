arr = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
for i in arr:
    if str(len(i))<str(len(i+1)):
        big = arr[i+1]
print(big)
# print(*arr)
# n=0
# for i in range(len(arr)):
#     for j in range(arr[i]):
#         j+=1
# print(j)