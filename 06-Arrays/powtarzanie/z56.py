def flatten_array(arr):
    """
    Converts a 2D array into a 1D array.
    """
    flattened = [element for row in arr for element in row]
    return flattened

print(flatten_array([[2, 3],
    [1, 5]]))

print(flatten_array([[5, 0, 3, 7, 5],[9, 0, 9, 1, 2]]))