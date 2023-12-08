import re
with open("15.txt", 'r', encoding='utf-8') as f:
    file_content = f.read()
    pattern = re.compile(r'\b\w{6,}\b')  
    words = pattern.findall(file_content)
    for word in words:
        print(word)
    print(words)



