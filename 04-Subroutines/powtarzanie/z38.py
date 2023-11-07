def f(palindrome):
    a= palindrome[::-1]
    if palindrome == a:
        return True
    else:
        return False

print(f("radar"))
print(f("12-11-21"))
print(f("book"))