from stack import pop, push, display, empty

push(10)
push(20)
push(30)

print("Stack: ")
display()

p_v = pop()
print(f"Popped value: {p_v}")

print("Is the stack empty?", empty())

print("Update Stack: ")
display()