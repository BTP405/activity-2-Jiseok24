# Write a Python function wordCount(t) which retrives data in a text file t and returns a dictionary where the keys are unique words in the files
# and the corresponding values are lists of line numbers where the words are found in the text.

# function wordCount()
def wordCount(t):
    dictionary = {}
    file = open(t, 'r')
    for line in file:
        words = line.split()
        for word in words:
            # Remove punctuation marks and convert to lowercase
            word = word.strip().lower()
            if word not in dictionary:
                dictionary[word] = 1
            else:
                dictionary[word] += 1
    return dictionary

filename = "sample.txt" 
print(wordCount("sample.txt"))