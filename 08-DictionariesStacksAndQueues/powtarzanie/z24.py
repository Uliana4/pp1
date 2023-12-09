# from stack import push, pop, empty, display

# def dec_to_bin(number):
#     # Initialize an empty stack to store remainders
#     remainder_stack = []

#     # Copy of the original number for display
#     original_number = number

#     # Convert the decimal number to binary using the stack
#     while number > 0:
#         remainder = number % 2
#         push(remainder)
#         number //= 2

#     # Display the division steps and remainders
#     print("Division\tRemainder")
#     while not empty():
#         remainder = pop()
#         print(f"{original_number} / 2 = {original_number // 2}\t{remainder}")
#         original_number = original_number // 2

#     # Display the final result
#     print(f"Natural number: {original_number}")
#     print("Binary number:", end=" ")
#     while not empty():
#         print(pop(), end="")
#     print()

# # Example: Convert the natural number 18 to binary
# dec_to_bin(18)

from stack import push, pop, empty, display

def dec_to_bin(number):
    # Initialize an empty stack to store remainders
    remainder_stack = []
    n1 = number
    # Copy of the original number for display
    original_number = number

    # Convert the decimal number to binary using the stack
    while number > 0:
        remainder = number % 2
        push(remainder, remainder_stack)  # Updated line
        number //= 2

    # Display the division steps and remainders
    print("Division\tRemainder")
    while not empty(remainder_stack):  # Updated line
        remainder = pop(remainder_stack)  # Updated line
        print(f"{original_number} / 2 = {original_number // 2}\t{remainder}")
        original_number = original_number // 2

    # Display the final result
    print(f"Natural number: {n1}")
    print("Binary number:", end = " ")
    while not empty(remainder_stack):  # Updated line
        print(pop(remainder_stack), end="")  # Updated line
    print()

# Example: Convert the natural number 18 to binary
dec_to_bin(18)
