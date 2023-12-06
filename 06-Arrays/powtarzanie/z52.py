array=[
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]
]

print("Array before swapping:")
for row in array:
    print(row)

a = array[0][4], array[1][4], array[2][4]
# Swap the first and last columns
array[0][4], array[1][4], array[2][4] = array[0][0], array[1][0], array[2][0]
array[0][0], array[1][0], array[2][0] = a
# Display the array after the changes
print("\nArray after swapping:")
for row in array:
    print(row)