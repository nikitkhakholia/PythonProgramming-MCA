## Question
''' You are a “Marvel” fan and today you feel like binging few movies of Marvel. Unfortunately you are struck in 
    CAT2 exam of Python. You are irritated but being the “Cool Geek” you figure out to involve Marvel in your code. 
    Write a class called”Love_For_Marvel” with an instance variable called “famous_quote”(String datatype) and method 
    called print_the_quote, it prints the famous_quote. but it is little strange, it is jumbled with numbers and the 
    method should reorder it and print the proper quote. Consider the following example and run your program for the 
    given two testcases. Create an object of the class and call the method.

    Example:
      famous_quote =” t1his dam3n cr4azy i2s” , the method print_the_quote () will print ->”this is damn crazy”

    Test case 1:
      famous_quote =”thi7s The1re Star5k wa2s kno6ws ide4a a3n” print_the_quote () will print ->” There was an idea Stark knows this”
    Test case 2:
      famous_quote =”foo6lish wi2se Th1e bri4dges whi5le buil3d barr7iers”, print_the_quote () will print->” The wise build bridges while foolish barriers." '''

## Answer
"""
This is a python 3 code written by @Nikit_Khakholia on 13 Oct 2021
"""

import re
# defining class


class Love_For_Marvel:

    # init function
    def __init__(self, inputQuote) -> None:

        # initializing instance variable
        self.famous_quote = ""

        # spliting the input to further process
        splittedString = inputQuote.split(" ")

        "for number of words given in input..."
        for index in range(len(splittedString)):

            "...check each word...."
            for word in splittedString:

                "...if the ordered index is present in it, if present..."
                if len(re.findall(str(index+1), word)) > 0:

                    "...append the word to the instance variable after removing the order integer."
                    self.famous_quote += ''.join(
                        [i for i in word if not i.isdigit()]) + " "

    # function to print the quote
    def print_the_quote(self):
        print(self.famous_quote)

print("Enter 'q' to exit program")
while True:

    # taking input from user
    jumbledString = input("Enter string jumbled with numbers: ")

    # flag variable for input validation
    validInput=True

    # handle quit
    if(jumbledString=='q'):
        exit()
    
    # checking empty input
    if not jumbledString:
        print('Invalid Input.. Try Again')
        validInput=False
    
    # checking if only one order integer is present in each word
    for word in jumbledString.split(' '):
        if(len([i for i in word if i.isdigit()]) != 1):
            print('Invalid Input.. Try Again')
            validInput=False

    # if the input is valid creating object
    if validInput:
        
        # initializing object
        lom=Love_For_Marvel(jumbledString)

        # calling print method
        lom.print_the_quote()
