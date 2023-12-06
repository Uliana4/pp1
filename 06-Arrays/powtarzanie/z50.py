array = [[-38,19],[5,40],[-7,11],[29,16]]

smallest_value = float('inf')  # Set to positive infinity initially
largest_value = float('-inf')  # Set to negative infinity initially
smallest_row = largest_row = smallest_col = largest_col = None

# Iterate through the array to find the smallest and largest values and their indices
for i in range(len(array)):
    for j in range(len(array[i])):
        current_value = array[i][j]

        # Check for the smallest value
        if current_value < smallest_value:
            smallest_value = current_value
            smallest_row, smallest_col = i, j

        # Check for the largest value
        if current_value > largest_value:
            largest_value = current_value
            largest_row, largest_col = i, j

# Display the results
print(f"Smallest Value: {smallest_value} at Row {smallest_row + 1}, Column {smallest_col + 1}")
print(f"Largest Value: {largest_value} at Row {largest_row + 1}, Column {largest_col + 1}")