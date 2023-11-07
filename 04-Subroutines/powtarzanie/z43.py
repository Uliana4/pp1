def f(name):
    return "".join(i[0].upper() for i in name.split())

print(f("Internet of Things"))
print(f("For Your Information"))
print(f("Python"))