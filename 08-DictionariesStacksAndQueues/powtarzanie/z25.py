from stack import push, pop, empty, display

def calculate_rpn(expression):
    stack = []

    # Split the expression into tokens
    tokens = expression.split()

    for token in tokens:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            # If the token is a number, push it onto the stack
            push(int(token), stack)
        elif token in ['+', '-', '*', '/']:
            # If the token is an operator, pop two items, perform the operation, and push the result
            operand2 = pop(stack)
            operand1 = pop(stack)

            if operand1 is not None and operand2 is not None:
                result = perform_operation(operand1, operand2, token)
                push(result, stack)
            else:
                print("Invalid RPN expression.")
                return
        elif token == '=':
            # If the token is '=', display the result
            result = pop(stack)
            if result is not None and empty(stack):
                print("Result:", result)
            else:
                print("Invalid RPN expression.")
                return
        else:
            print("Invalid token:", token)
            return

    if not empty(stack):
        print("Invalid RPN expression.")
        return

def perform_operation(operand1, operand2, operator):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        if operand2 == 0:
            print("Error: Division by zero.")
            exit()
        return operand1 / operand2

# Examples
calculate_rpn("2 3 + =")            # 2 + 3
calculate_rpn("2 4 1 + * =")        # 2 * (4 + 1)
calculate_rpn("2 3 + 4 5 + * =")    # (2 + 3) * (4 + 5)
calculate_rpn("8 3 1 + / 3 2 - 4 + * =")  # 8 / (3 + 1) * (3 - 2 + 4)