import re
text = "To be, or not to be, that is the question"
numb_vowels= re.findall(r'[aeioquyAEIOQUY]', text)
print(len(numb_vowels)) 