## Question
''' Consider the csv file “winemag-data_first150k.csv”. Do the following actions
      1. Remove all records which have missing data
      2. Group the records by country
      3. Print the description and winery name of costliest wine in Spain.
      4. Find average points for each country.
'''

## Answer
# This is Python 3 code 
# Developed by @Nikit Khakholia
# On 18 October 2021

# importing pandas as pd
import pandas as pd

# reading csv data and storing it in variable data
data = pd.read_csv("/Users/nikit/Desktop/Python/Lab/winemag-data_first150k.csv")

# cleaning data
cleanedData = data.dropna()

# grouping data by country
groupedData = data.groupby("country").describe()

# selecting only spain data from the dataset
spainData = data[data['country']=='Spain']
# selecting index of maximum price in the spainData
maxIndex = spainData["price"].idxmax()
# printing data from the revieved index
print("Winery: "+data.loc[maxIndex]['winery'])
print("Description: "+data.loc[maxIndex]['description'])


print("\n\n\n\n")



# grouping data by country and selecting average points for each country
avgPoints = data.groupby("country").points.mean()
print(avgPoints)
