arr = [2,3,7,5,4]
for n in arr:
    print(n)
print(arr)
print(len(arr))
print(arr[0])
print(arr[1])
print(arr[-1])
print(len(arr)-1)
print(len(arr)//2)
sum = 0
sum+=arr[0]+arr[-1]
print(sum)

s = 0
for i in range(len(arr)):
    s += arr[i]
print(s/len(arr))

# h
middle_index = len(arr) // 2
middle_value = arr[middle_index]
print(f"h. Middle value: {middle_value}")

i=0
while i<len(arr):
    print(arr[i], end = " ")
    i+=1