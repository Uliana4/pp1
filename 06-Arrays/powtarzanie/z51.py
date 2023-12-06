array=[
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]
]

print("Array before swapping:")
for row in array:
    print(row)

# Swap the first and last rows
array[0], array[2] = array[2], array[0]

# Display the array after the changes
print("\nArray after swapping:")
for row in array:
    print(row)