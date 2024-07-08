letters = {
    "e": "3",
    "A": "4",
    "b": "6",
    "B": "8",
    "o": "0",
    "I": "1",
    "S": "5",
    "f": "7",
    "p": "9",
    "Z": "2"
}

def replaceLetters(word, letters_dict):
    replacedWord = ""
    for char in word:
        if char in letters_dict:
            replacedWord += letters_dict[char]
        else:
            replacedWord += char
    return replacedWord

orgWord = "Hello, I am a Bot"
print(replaceLetters(orgWord, letters))