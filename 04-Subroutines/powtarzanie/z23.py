def times(text):
    a = "e"
    count= 0
    for i in text:
        if a in i:
            count+=1
    return f"The number of letter '{a}': {count}"

print(times("You never get a second chance to make a first impression"))