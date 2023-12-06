m = [
[1,2,3],
[4,5,6],
[7,8,9]
]
 
transposed = [list(row) for row in zip(*m)]
print (transposed)


# def transpose_matrix(m):
#     """
#     Transposes the given matrix m.
#     """
#     # Use zip to transpose the matrix
#     transposed = [list(row) for row in zip(*m)]
#     return transposed

# def display_matrix(arr):
#     """
#     Displays a 2D array in rows and columns.
#     """
#     for row in arr:
#         for element in row:
#             print(element, end=" ")
#         print()

# # Given matrices
# matrix_a = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# matrix_b = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 0]
# ]

# matrix_c = [
#     [5, 6, 7, 8]
# ]

# # Display original and transposed matrices
# matrices = [matrix_a, matrix_b, matrix_c]

# for i, matrix in enumerate(matrices, start=1):
#     print(f"\nMatrix {chr(ord('a') + i)} (Original):")
#     display_matrix(matrix)

#     transposed_matrix = transpose_matrix(matrix)
    
#     print(f"\nMatrix {chr(ord('a') + i)} (Transposed):")
#     display_matrix(transposed_matrix)
