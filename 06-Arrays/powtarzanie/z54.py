def transpose_matrix(m):
    transposed = [list(row) for row in zip(*m)]
    return transposed
    
for i in transpose_matrix([[1, 2, 3],[4, 5, 6],[7, 8, 9]]):  
    print (i)

print(transpose_matrix([[1,2,3],[4,5,6], [7,8,9]]))

# Example usage:
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# transposed_matrix = transpose_matrix(matrix)

# # Display the original and transposed matrices
# print("Original Matrix:")
# for row in matrix:
#     print(row)

# print("\nTransposed Matrix:")
# for row in transposed_matrix:
#     print(row)