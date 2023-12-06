def count_words(text):
    words = text.split() # split the text into a list of words
    return len(words) 
print(count_words('An apple a day keeps the doctor away'))

def ordered_array_of_words(text):
    # Sort the words in descending order of their lengths
    words = text.split()
    sorted_words = sorted(words, key=lambda x: len(x), reverse=True)
    return sorted_words
print(ordered_array_of_words('An apple a day keeps the doctor away'))

def sorted_words(text):
    words = text.lower().split()
    words.sort()
    return words
print(sorted_words('An apple a day keeps the doctor away'))