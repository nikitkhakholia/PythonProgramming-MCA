## Question
# You are an enigmatologist, a person who loves riddles, puzzles. 
# Morse code has always fascinated you and in today’s lab you 
# want to include your love for riddles in the code you write.
#    a) Write a python script which takes in a string and converts 
#    it into the Morse code and prints it. Include one space after each character
#    b) Write a script which accepts Morse code and prints back English words in camel case.
# Use dictionary or list comprehensions wherever you feel is required.

# Test Case:
# Input = “Seriously!”
# Output=”… . .-. .. --- ..- … .-.. -.-- -.-.--"
# Input=”… . .-. .. --- ..- … .-.. -.-- -.-.--"
# Output=”“Seriously!”

# Note :
# The symbols for Morse code
# -> “.” Dot
# -> “-“ Dash(hyphen)
# The Morse code chart is given below
# Input for 1(a) can be both lower and upper case
# The Morse code should be printed with one space between each character
# The input for 1(b) should also take Morse code with space after each character

## Answer
# This is Python 3 code snippet
# Developed by Nikit Khakholia
# On 1 Sep 2021

# dictionary of morse codes
codesDictionary = {
    "a": ".-",    "b": "-...",    "c": "-.-.",    "d": "-..",    "e": ".",    "f": "..-.",    "g": "--.",    "h": "....",    "i": "..",    "j": ".---",    "k": "-.-",
    "l": ".-..",    "m": "--",    "n": "-.",    "o": "---",    "p": ".--.",    "q": "--.-",    "r": ".-.",    "s": "...",    "t": "-",    "u": "..-",    "v": "...-",
    "w": ".--",    "x": "-..-",    "y": "-.--",    "z": "--..",    "1": ".---",    "2": "..---",    "3": "...--",    "4": "....-",    "5": ".....",    "6": "-....",    "7": "--...",
    "8": "---..",    "9": "----.",    "0": "-----",    ".": ".-.-.-",    ",": "--..--",    "?": "..--..",    "!": "-.-.--",    "'": ".----.",
    "\"": ".-..-.",    "(": "-.--..",    ")": "-.--.-",    "&": ".-...",    ":": "---...",    ";": "-.-.-.",    "/": "-..-.",    "-": "..--.-",
    "=": "-...-",    "+": ".-.-.",    "-": "-....-",    "$": "...-..-",    "@": ".--.-.",
}

# list of morse code keys and values
characters = list(codesDictionary.keys())
codes = list(codesDictionary.values())

# run recursively to encode and decode
while True:

    # select action to encode or decode
    action = input("1. Encode    0. Decode\n")

    # encoding
    if(action == '1'):
        encoded = ""
        phrase = input("Enter text to encode: ")
        for char in phrase:
            encoded += codesDictionary[char.lower()]+" "
        print("Encoded: "+encoded)

    # decoding
    elif(action == '0'):
        decoded = ""
        phrase = input("Enter morse code to decode: ")
        for char in phrase.split(" "):
            decoded+=characters[codes.index(char)]
        print("Decoded: "+decoded[:1].upper()+decoded[1:])
    else:
        print("Please try again.")
