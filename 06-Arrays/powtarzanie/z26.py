arr = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
# for i in range(len(arr)):
#     str_i = str(i)
#     if len(str_i)<len(i+1):
#         big = arr[i+1]
# print(big)
longest_name = max(arr, key=len)
print(longest_name)