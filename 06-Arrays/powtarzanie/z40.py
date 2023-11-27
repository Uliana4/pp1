import numpy as np
arr = np.random.randint(1,999,8)
print(*arr) 

max_width = len(str(max(arr)))

# Create a horizontal line for the top and bottom of the formatted array
line = "-" * (max_width +1 )

# Print the top line
print(line * len(arr))

# Print the elements of the array in a formatted manner
formatted_array = "|"
for num in arr:
    formatted_array += f"{num:>{max_width}}|"

# Print the formatted array
print(formatted_array)

# Print the bottom line
print(line * len(arr))


# import random
# arr = [random.randint(1,999) for _ in range(8)]
# print(arr)