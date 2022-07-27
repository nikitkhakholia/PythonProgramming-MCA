## Question
''' Write the following functions and use “re” to get the solution
    1. Write a function named “LoveForFrenchFries” which takes in a string and returns the number of 
    times the word ”potato” is in the given string.
    Example:
      LoveForFrenchFries(“potato”)-> 1
      LoveForFrenchFries(“potatopotato”) ->2
    Note: Let the input string be of continuous letters like the above examples.
    2. Write a function “MyScottishAccent” which takes in a string and replaces every occurrence of “o” with “u”.
    Example:
      MyScottishAccent(“hello python coders”)->”hellu pythun cuders”
      MyScottishAccent(“computer nerd”)->”cumputer nerd”
    3. Write a function called “LinkVowels” which takes a string and returns True if one word ends with a vowel and the adjacent starts with a vowel.
    Example:
      LinkVowels(“code all functions”)->True ( “code” ends with vowel and “all” starts with vowel)
      LinkVowels(“ These crazi ones”)-> True (“These” ends with vowel and “are” starts with a vowel)
      LinkVowels(“This sucks”)-> False
    4. Write a function called “LonelyOne” which returns the number of “1’s” which are lonely. 1is lonely if it is not immediately followed by another 1.See the example for better understanding of “lonely”.
    Example:
      LonelyOne(101)-> 2 (“1” is lonely twice)
      LonelyOne(1111)->0
      LonelyOne(444)->0
    Note: You can take the input as a string also '''

## Answer
# This is Python 3 code snippet
# Developed by Nikit Khakholia
# On 14 September 2021

'''A python script that demonstrates use of re module.'''

# importing re module
import re

# search number of occurence of a given string in a given string
def LoveForFrenchFries(frenchFries):
    return len(re.findall('potato',frenchFries))
print(LoveForFrenchFries(input("Enter french fry to search for potato.\n")))

# replace given character with given character in the given string
def MyScottishAccent(sentence):
    return re.sub('o','u',sentence)
print(MyScottishAccent(input("Enter Scotish.\n")))

# search for given patterns in the given string
def LinkVowels(sentence):
    return len(re.findall("[aeiou] [aeiou]",sentence))>0
print(LinkVowels(input("Enter the sentence for LinkVowels\n")))

# search for given character with conditions in given string
def LonelyOne(number):
    return len(re.findall("(?<!1)1(?!1)", number))
print(LonelyOne(input("Want count of lonely 1's.. Enter the number\n")))
