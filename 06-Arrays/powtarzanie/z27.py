arr=[12,6,4,9,10]
def star(n):
    if n in arr:
        for i in arr:
            i=n*"*"
        return (f'{n}: {i}')
print(star(12))
