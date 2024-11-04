def bookWordCount(book):
    return len(book.split())

def countLetters(book):
    letters = dict()
    for char in book.lower():
        if char.isalpha():
            if (char in letters):
                letters[char] += 1
            else:
                letters[char] = 1
    return letters

book = open("books/frankenstein.txt").read()

wordCount = bookWordCount(book)
letterFrequencies = countLetters(book)

print(f"this book is {wordCount} words long")

for letter, frequency in letterFrequencies.items():
    print(f"the letter {letter} appears {frequency} times")

