## Question
''' The current pandemic situation has disturbed you a lot.As a programmer you 
    want to write a python script for it . Write a function which accepts the 
    map and prints the following
      · Changed map after applying the rules
      · Percentage of people affected
      · Number of continents in the map
    Consider the following information and rules
      -> The input map consisting of “0”,”1”,”X”.
      -> “0” indicates the person is not infected
      -> “1” indicates that the person is infected
      -> “X” indicates ocean.
    Rules
      a) Infection cannot crossover ocean.
      b) If one person is infected rest all will be infected.
      c) First and last continent are not connected.
    Example
      Input Map: “01000000X000X011X0”
      Output:
        Map after rule applied: “11111111X000X111X0”
    (If one is affected all are affected in the continent , infection cannot cross over continent)

    Percentage of people infected :
      Total number of people are : 15
      Infected are : 11
      Percentage affected will be 11*100/15 = 73.33
      Number of continents =4
    
    Use the following test cases
      1.  Input = “001X11000000X00000X1”
          Output = “111X11111111X00000X1”
          Percentage affected=70.58
          Number of continents=4
      2.  Input=”111X00000X0101X0”
          Output-“111X00000X1111X0”
          Number of continents=4
          Percentage affected=53.84
      3.  Input = “0000110001110000011”
          Output=“1111111111111111111”
          Percentage affected =100
          Number of continents=0 '''

## Answer
import re

def checkInfection(tests):
    if(len(re.findall("[^01X]",tests))>0):
        print("Invalid Input")
        return
    continents = tests.split('X')
    outputString = ""
    for continent in continents:
        if(len(re.findall('1', continent)) > 0):
            outputString += re.sub('0', '1', continent)+"X"
        else:
            outputString += continent+"X"
    print("Input: "+tests)
    print("Output: "+outputString[:-1])
    print("Percentage affected: " + str(round((len(re.findall('1', outputString)) / (len(tests)-len(re.findall('X', tests))))*100,2)))
    print("Number of continents: "+str(len(continents)))


while True:
    checkInfection(input("Enter tests string.\n"))
    print("\n\n")
