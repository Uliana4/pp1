import re
text = "To be, or not to be, that is the question"
words = re.split(r'\s',text)
# re.findall(r'\b\w+\b' , text)
print(len(words))