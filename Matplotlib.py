## Question
''' Consider the csv file “sales_data_sample.csv”. Do the following actions
      1. Read all the sales and plot the same using an appropriate plot type
      2. Plot the quarterly sales using an appropriate plot type
'''

## Answer
# This is Python 3 code 
# Developed by @Nikit Khakholia
# On 27 October 2021

#importing pandas as pd and matplotlib as plt
import pandas as pd
import matplotlib.pyplot as plt

#reading the csv file in data
data = pd.read_csv("/Users/nikit/Desktop/Python/Lab/sales_data_sample.csv",encoding = 'latin1')
# printing data
print(data)

#plotting year and sales in bar graph
plt.bar(data['YEAR_ID'],data['SALES'],color = 'black',width=0.4)
plt.show()


#separating quaterly data from full data
q1 = data.loc[data['QTR_ID']==1]
q2 = data.loc[data['QTR_ID']==2]
q3 = data.loc[data['QTR_ID']==3]
q4 = data.loc[data['QTR_ID']==4]

# plotting bars for quater
plt.bar(q1['QTR_ID'],q1['SALES'],)
plt.bar(q2['QTR_ID'],q2['SALES'],)
plt.bar(q3['QTR_ID'],q3['SALES'],)
plt.bar(q4['QTR_ID'],q4['SALES'],)

# putting x label
plt.xlabel("QUARTER")

# putting y label
plt.ylabel("SALES")

# showing column names
plt.legend(["Q1","Q2","Q3","Q4"])

# showing graph
plt.show()
