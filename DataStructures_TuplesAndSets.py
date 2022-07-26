## Question
# You sometimes “binge-watch” series and recently you watched 
# “Scam 1992” in SonyLIV. You were fascinated by the main character 
# and also find stock market trading interesting. As a “Python Guru”, 
# you want to write a python script for helping a stock broker in his 
# day-to-day activity. You encounter the following problem and write 
# a solution to it

# A stock broker receives from his client instructions to buy and sell 
# shares in form of a tuple. He understands the instructions and 
# completes the trading but finds it difficult to send total amount 
# spent on buying and total amount received by selling as tuple. 
# So you help the stock broker by printing it as a string. 
# Consider the explanation and following test case

# Input is a tuple which contains tuples as elements
# Each element in the tuple will have Company initials, 
# quantity, price, status where status is buy(b) or sell(s)

# -> If the input is ((“ABC”,300,453.0,”b”),(“XYZ”,120,298.5,”s”),
#    (“ASD”,29,45.5,”s”),(“QWE”,160,23,7,”b”))
#    Output will be “Buys: 139692 Sell:4901.5”
# -> If input is empty tuple print “Buys: 0 Sell:0”
# -> If the input is not as per format required for example
#    (“SDF”,200,4.5,”l”) print “Invalid input”

# Note: The stock broker is quite busy throughout the day 
# so run the program to accept input iteratively, till the 
# broker says “I am gonna call it night”

## Answer
# This is Python 3 code snippet
# Developed by Nikit Khakholia
# On 30 August 2021

# flag variable to calculate for more clients
moreClients = True
# keep calculating while falg is true
while moreClients:
    action = input("1. Calculate 0. Exit\n")
    if(action == "1"):
        # flag to insert transaction for the client
        takeInput = True
        buys = 0.0
        sell = 0.0
        while takeInput:
            insert = input("1.Insert 0: Exit\n")
            if insert == '1':
                try:
                    # input details into tuple
                    transaction = tuple((input("Company: "), float(input("Quantity: ")),
                                     float(input("Price: ")), input("Buy/Sell (b/s): ")))

                    # calculating buys and sell values
                    if transaction[3] == "b":
                        buys += transaction[1]*transaction[2]
                    elif transaction[3] == "s":
                        sell += transaction[1]*transaction[2]
                    else:
                        print("Invalid Input")
                        break
                except:
                    print("Invalid Input")
                    break
            elif insert == '0':
                # stop taking input for the client
                takeInput = False
                print("Buys: "+str(buys)+" Sell: "+str(sell))
            else:
                print("Try Again...")
    elif action == "0":
        # exit program
        moreClients = False
    else:
        print("Try Again...")
