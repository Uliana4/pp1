array=[7,3,8,5,2]
print(array)
# for i in range(len(array)):
#     for j in range(0, len(array)- i - 1):
#         mod = max(array[j])
#     print(max(array[j]))
for i in array:
    maxn=max(array)
    minx=min(array)
    med = maxn-minx
print(med)
print(minx,",",maxn)

# for i in array:
#     i = i+'-'
# print(array)