def bookWordCount(book):
    return len(book.split())

def letterFrequency(book):
    letters = dict()
    for char in book.read().lower():
        if char.isalpha():
            if (char in letters):
                letters[char] += 1
            else:
                letters[char] = 1
    return letters

book = open("books/frankenstein.txt")



