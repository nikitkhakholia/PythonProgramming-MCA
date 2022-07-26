## Question
# Suddenly today morning your “Python” course teacher gets interested 
# in joining social networking site! The signup page requires her to 
# input name and a password. But the password must be strong. The website 
# considers a password to be strong if it satisfies the given criteria:
# -> Its length is at least 8.
# -> It contains at least one digit. (0123456789)
# -> It contains at least one lowercase English alphabet. (abcdefghijklmnopqrstuvwxyz)
# -> It contains at least one uppercase English alphabet. (ABCDEFGHIJKLMNOPQRSTUVWXYZ)
# -> It contains at least one valid special character. The valid special characters are: !@#$%^&*
# She typed a random string of length in the password field but isn’t sure if it is strong. 
# You are her pet student and a “Python Geek” so she sends you a message to check 
# if her password is strong and if not suggest her a good password.

# Write a python script which accepts the password as input and checks 
# if it is strong or not. If it is strong print the following statement 
# “Secure Password! Go Ahead and Register.” Else suggest a strong password.
# You need to use lambda functions for checking if the password is strong 
# or not and also to create a strong password.
# Note: When input is a weak password print new password every time you run the script

## Answer
# This is Python 3 code snippet
# Developed by Nikit Khakholia
# On 6 Sep 2021

import re
import random

# lambda function for special char
specialChars = lambda chars : len(re.findall("[!@#$%^&]", chars)) > 0

# lambda function for upper case
capsChars = lambda chars : len(re.findall("[A-Z]", chars)) > 0

# lambda function for small case
smallChars = lambda chars : len(re.findall("[a-z]", chars)) > 0

# lambda function for digits 
digitChars = lambda chars : len(re.findall("[0-9]", chars)) > 0

# lambda function for 8 chars
minChars = lambda chars : len(chars) >= 8

# take password to test
password = input("Enter password to test.\n")

# if all lambda functions returns true
if(specialChars(password) and capsChars(password) and smallChars(password) and digitChars(password) and minChars(password)):
    print("Secure Password! Go Ahead and Register.")

# else generate a new password
else:
    print("Generating new password.")
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']

    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
               '*', '(', ')', '<']
    newPassword = random.choice(DIGITS)+random.choice(UPCASE_CHARACTERS)+random.choice(LOCASE_CHARACTERS)+random.choice(
        SYMBOLS)+random.choice(DIGITS)+random.choice(UPCASE_CHARACTERS)+random.choice(LOCASE_CHARACTERS)+random.choice(SYMBOLS)
    print(newPassword)
