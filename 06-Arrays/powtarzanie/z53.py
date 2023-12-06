def identity_matrix(n):
    a = [[0] * n for _ in range(n)]
    for i in range(n):
        a[i][i] =1 
    return a   

def display_array(arr):
    """
    Displays a 2D array in rows and columns.
    """
    for row in arr:
        for element in row:
            print(element, end=" ")
        print()


dimensions = [3, 5, 8]

for dimension in dimensions:
    # Generate and display the identity matrix
    identity_mat = identity_matrix(dimension)
    
    print(f"\nIdentity Matrix of Size {dimension}:\n")
    display_array(identity_mat)

# print(identity_matrix(8))