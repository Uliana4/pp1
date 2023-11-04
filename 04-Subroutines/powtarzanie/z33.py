def f(n):
    if n>1:
        return (n-1) * "*/" + "*"
    else:
        return n*"*"

print(f(4))
print(f(1))
print(f(8))