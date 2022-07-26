## Question
''' Create a module named “OMG” with the functions “ValidateCreditCard” and “ALLISWELL” in it. 
    Call these functions into another python script by importing the module “OMG”. The details 
    of the functions are given below
    A bank named PCC(PythonCodeChallenge) is in serious trouble. They are encountering numerous 
    cases of invalid credit cards of their bank in use. You are a Python geek of 1 MCA and the 
    Chief Technical Officer (CTO ) wants you to take up the job “security expert” in the bank. 
    Though they are convinced of your skillset, the technical team lead wants one final test, 
    to write a python program described below as your “Lab 5 “Exercise.

    I. Create a function called ValidateCreditCard which takes input a credit card number name 
    the variable as “ ccnumber” and returns isvalid – a Boolean variable. Check if the ccnumber 
    is valid or not and assign “True” or “False”to the variable isvalid. The rules for a Credit 
    Card number to be valid are given below
          1. The number should have minimum of 14 digits and maximum of 19. If not in the 
          mentioned range return ”False”
          2. If the number is in the range mentioned then do the following steps to check 
          if the ccnumber is valid
              a. Remove the last digit.
              b. Reverse the number
              c. Double the digits which are in odd numbered positions. If the doubled value is a double digit then add the digits (for eg if ‘5’ is doubled we get 5*2=10 which is double digit so add 1+0=1)
              d. Add all the digits now
              e. Subtract the last digit from the sum obtained in “d” from 10.
              f. If the result is same as the last digit from step “a” then your card number is valid
    Sample Test Case
      If the ccnumber is 1234567890123456
        Step a: last digit = 6, ccnumber = 123456789012345
        Step b: ccnumber reversed = 543210987654321
        Step c: After selective doubling: [1, 4, 6, 2, 2, 0, 9, 8, 5, 6, 1, 4, 6, 2, 2]
        Step d: sum = 58
        Step e: 10 - 8 = 2
        Step f: (not equal to 6) validity=false
        
    II. Create another function called “ALLISWELL” this takes in a Boolean value and prints 
    the statement “ALL IS WELL!” twice if input is “False” and once if input is “True”.'''

## Answer
# omg.py
def ValidateCreditCard(ccnumber):
    c1 = list(map(int, ccnumber[:-1][::-1].strip()))
    i = 1
    for n in c1:
        # print(n)
        if i % 2 == 0:
            pass
        else:
            c1[i-1] = n*2 if n * 2 < 10 else sum(map(int, str(n*2)))
        i = i+1
    if(not( len(ccnumber) < 14 and len(ccnumber) > 19) and 10-(sum(c1)%10) == int(ccnumber[-1])):
        return True
    else:
        return False


def ALLISWELL(x): 
    if(x):
        print("ALL IS WELL!")
    else:
        print("ALL IS WELL!")
        print("ALL IS WELL!")

# omgallizzwell.py
import omg
print("Validate your Credit Card here.")
if(omg.ValidateCreditCard(input("Enter your credit card number below.\n"))):
    print('Valid Card')
else:
    print('Invalid Card')

while True:
    x=input("Welcome to ALLISWELL test.\n1. True    0. False\n")
    if(x=='1'):
        omg.ALLISWELL(True)
    elif(x=='0'):
        omg.ALLISWELL(False)
    else:
        print("Wrong Input")
