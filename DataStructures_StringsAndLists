# You cannot imagine world without “Alphabet Inc”! 
# You are also an ardent fan of its COE !
# As a true fan you want to write a code involving “Google”.

## Question 1
# Write a script named “GooglePassion” that takes input a 
# list and prints as output a string . Your input should be 
# numbers having 1,2,3,4,5,6,7,8(zero and nine are not be included). 
# Consider the following rules for returning the string
# -> 1, 2, 3, 4 = g, o, l, e
# -> 5 indicates to up case of letter before it.
# -> 6 indicates Add a point to the end.
# -> 7 indicates Change case of the first letter.
# -> 8 indicates Reverse the string.
# Consider the example
# Input is ([“12213467”]), Output is "Google."

## Answer
# This is Python 3 code snippet
# Developed by Nikit Khakholia
# On 25 August 2021

'''A script that takes input a list and prints as output a string.
Rules
    · 1, 2, 3, 4 = g, o, l, e
    · 5 indicates to up case of letter before it.
    · 6 indicates Add a point to the end.
    · 7 indicates Change case of the first letter.
    · 8 indicates Reverse the string.'''

# variables declared
# string to store output
outputString = ""
# string to store input chars
inputList = ""

# handle alphabet chars
try:
    inputList = str(int(input("Enter numbers between 1 -8.\n")))
    # validate 9 and 0 are not present
    if(inputList.find('9')>-1 or inputList.find('0')>-1):
        print("Invalid numbers found.\nExiting...")
        exit()
# exit if alphabets are entered
except:
    print("Enter numbers between 1-8 only.\n Try Again.")
    exit()

# traverse through input string and make changes accouding to rules
for number in inputList:
    if(number == '1'):
        outputString += 'g'
    elif(number == '2'):
        outputString += 'o'
    elif(number == '3'):
        outputString += 'l'
    elif(number == '4'):
        outputString += 'e'
    elif(number == '5'):
        outputString = outputString[0:(len(outputString)-1)]+outputString[(len(outputString)-1):(len(outputString))].upper()
    elif(number == '6'):
        outputString += '.'
    elif(number == '7'):
        outputString = outputString[0:1].upper()+outputString[1:(len(outputString))]
    elif(number == '8'):
        outputString = outputString[::-1]

print("Output: ",outputString)


#----------------------------------------------------------------------
## Question 2
# You are an excellent “English Linguist” and also love to 
# code in Python. Write a python script “connect” that connects 
# each previous word to the next word. Print the resulting 
# string (removing duplicate characters in the overlap). More 
# specifically, look at the overlap between the previous words 
# ending letters and the next word's beginning letters.
# Example connect(["move", "over", "very"]) gives [“movery”]

## Answer
# This is Python 3 code snippet
# Developed by Nikit Khakholia
# On 25 August 2021

'''A python script that connects each previous word to the next word.'''
print("Enter words. Enter 0 for output.")

# variables declared
# flag for taking input
takeInput = True                                  
# list to store input words
inputWords = [] 

# loop to take multiple inputs
while takeInput:                   
    word = input("Word: ")
    # change input flag and stop taking input
    if(word=='0'):
        takeInput=False 
    elif(word.strip()=='' ):
        print("Invalid Word...")
    # store word in list      
    else:
        inputWords.append(word.strip())  

# traverse list      
for wordIndex in range(len(inputWords)-1):
    # flag to store if the word is overlaped
    overlaped=False
    # taking two words at a time check if the smaller word is overlaped for each part of the word in reverse order
    for x in reversed(range(1,1+(len(inputWords[wordIndex]) if len(inputWords[wordIndex])<len(inputWords[wordIndex+1]) else len(inputWords[wordIndex+1])))):
        # store the remaining part of 2nd word if its overlaped and mark flag as true
        if(inputWords[wordIndex][(-1*(x)):]==inputWords[wordIndex+1][:x]):
            inputWords[0]+=inputWords[wordIndex+1][x:]
            overlaped=True
            break
    # append the whole word as it is not overlaped
    if not overlaped:
        inputWords[0]+=inputWords[wordIndex+1]

print("Output: ",inputWords[0])
