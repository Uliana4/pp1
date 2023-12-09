# stack.py

stack = []

def push(value, custom_stack=None):
    stack_to_use = custom_stack if custom_stack is not None else stack
    stack_to_use.append(value)

def pop(custom_stack=None):
    stack_to_use = custom_stack if custom_stack is not None else stack
    if not empty(custom_stack):
        return stack_to_use.pop()
    else:
        return None

def empty(custom_stack=None):
    stack_to_use = custom_stack if custom_stack is not None else stack
    return len(stack_to_use) == 0

def display(custom_stack=None):
    stack_to_use = custom_stack if custom_stack is not None else stack
    for i in range(len(stack_to_use)-1, -1, -1):
        print(stack_to_use[i])
    print()
