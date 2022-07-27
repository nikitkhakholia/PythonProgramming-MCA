## Question
''' You are “Live Wire”( a person who has a lot of energy and is interesting to be with) and have many friends in your 
    MCA class. You also got interested in the Zodiac signs and the have read characteristics of each sign. Today morning 
    you feel like making each one of your friend’s birthday’s special. What better than writing a python program! You want 
    your friends to run the program you write.
    
    Write a program which accepts as input a DOB in the format “dd/mm/yyyy “and prints one positive quality of the Zodiac 
    sign he/she belongs to. Validate the input
        · If no input is given print your zodiac sign positive quality
        · If “?” is typed help the user by telling him/her to enter Data of Birth in the required format
        · If date is entered validate the correctness of the date
        · If “q” or “Q” is entered invoke a user defined exception which quits the program after printing “Bye! Hope you run this program again”.'''

## Answer
# This is Python 3 code snippet
# Developed by @Nikit Khakholia
# On 2 October 2021
from datetime import date
import re
'''A python script that demonstrates exception handling with custom exception.'''

# custom exception for format error
class FormatError(Exception):
    pass

# class to initialise sunshine based on dob
class Sunshine():
    def __init__(self, dob) -> None:
        # conditions for initializing zodiac and sunshine based on dob
        if((dob[1] == 3 and dob[0] >= 20) or (dob[1] == 4 and dob[0] < 19)):
            self.zodiac = 'Aries'
            self.desc = "Gets angry, then forgets why they were angry"
        elif((dob[1] == 4 and dob[0] >= 19) or (dob[1] == 5 and dob[0] < 20)):
            self.zodiac = 'Taurus'
            self.desc = "All or nothing, no in between"
        elif((dob[1] == 5 and dob[0] >= 20) or (dob[1] == 6 and dob[0] < 21)):
            self.zodiac = 'Gemini'
            self.desc = "Charismatic"
        elif((dob[1] == 6 and dob[0] >= 21) or (dob[1] == 7 and dob[0] < 22)):
            self.zodiac = 'Cancer'
            self.desc = "Only has one boundary, but it is very firm"
        elif((dob[1] == 7 and dob[0] >= 22) or (dob[1] == 8 and dob[0] < 22)):
            self.zodiac = 'Leo'
            self.desc = "Really big personality"
        elif((dob[1] == 8 and dob[0] >= 22) or (dob[1] == 9 and dob[0] < 22)):
            self.zodiac = 'Vigro'
            self.desc = "A million ideas per second"
        elif((dob[1] == 9 and dob[0] >= 22) or (dob[1] == 10 and dob[0] < 23)):
            self.zodiac = 'Libra'
            self.desc = "Really good aesthetics"
        elif((dob[1] == 10 and dob[0] >= 23) or (dob[1] == 11 and dob[0] < 22)):
            self.zodiac = 'Scorpio'
            self.desc = "Eyes that look into your soul"
        elif((dob[1] == 11 and dob[0] >= 22) or (dob[1] == 12 and dob[0] < 21)):
            self.zodiac = 'Sagittarius'
            self.desc = "Obsessed with self-improvement"
        elif((dob[1] == 12 and dob[0] >= 21) or (dob[1] == 1 and dob[0] < 19)):
            self.zodiac = 'Capricorn'
            self.desc = "The responsible friend"
        elif((dob[1] == 1 and dob[0] >= 19) or (dob[1] == 2 and dob[0] < 18)):
            self.zodiac = 'Aquarius'
            self.desc = "Purposefully esoteric"
        elif((dob[1] == 2 and dob[0] >= 18) or (dob[1] == 3 and dob[0] < 20)):
            self.zodiac = 'Pisces'
            self.desc = "Excessively romantic"
        else:
            self.zodiac = "Not found"
            self.desc = ""

# validation of input
def validateDob(dob) -> int:
    # try block to catch any exception raised
    try:
        if(len(dob) != 3):
            raise FormatError("Enter date of birth in DD/MM/YYYY format.")
        if(int(dob[0]) > 31 or int(dob[0]) < 1):
            raise Exception("Enter valid date.")
        if(int(dob[1]) > 12 or int(dob[1]) < 1):
            raise Exception("Enter valid month.")
        if(len(dob[2]) != 4 or int(dob[2]) > int(str(date.today()).split('-')[0])):
            raise Exception("Enter valid year.")
    # catching raised format errors
    except FormatError as e:
        print(e)
        return 0
    # catching any value errors
    except ValueError:
        print("Enter NUMBERS ONLY.")
        return 0
    # catchiing all other errors
    except Exception as e:
        print(e)
        return 0
    # if no error occured then return parsed date
    else:
        return [int(dob[0]), int(dob[1]), int(dob[2])]
    # finally block runs always
    finally:
        """This runs every time regardless of exception."""


# flag to run program recursively
quit = False

# running program recursively
while True:
    # taking input of dob
    dob = input("Enter your birthdate(DD/MM/YYYY): ")
    
    # check to quit program
    quit = len(re.findall("[Qq]", dob)) > 0
    
    # default date if no input is entered
    if len(dob) == 0:
        dob = "9/3/1999"

    # run the program
    if (not quit):
        # validating the input
        dobValidated = validateDob(dob.split("/"))
        
        # if validated print sunshine
        if dobValidated:
            # initializing sunshine object
            data = Sunshine(dobValidated)
            print(data.zodiac+"- "+data.desc)
    # quit the program
    else:
        print("Bye!!")
        exit()
