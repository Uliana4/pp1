import random

def rand_elem(array):
    if not array:  # if the array is empty, return None
        return None
    return random.choice(array)

my_array = [1, 2, 3, 4, 5]

print(rand_elem(my_array))
print(rand_elem(my_array))
print(rand_elem(my_array))