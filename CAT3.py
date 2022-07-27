## Question
''' The dataset named ““AircraftWildlifeIncident.csv” contains details of bird attack on aircraft. The columns are Record ID, 
    Incident Year, Incident Month, Incident Day, Operator ID, Operator, Aircraft, Aircraft Type, Aircraft Make, Aircraft Model, 
    Species ID, Species Name, Species Quantity, Aircraft Damage.
    
    Consider the csv file “AircraftWildlifeIncident.csv” and perform the following
      1. Read the csv file and create and print a data frame.
      2. Find if any missing values (null values) are in the data, delete all the rows with missing data and print the data frame.
      3. Group by year and print the count of number of incidents in a year.
      4. Print the count of incidents when the Species is “MUNIAS”
'''

## Answer
# This is Python 3 code
# Developed by @Nikit Khakholia
# On 27 October 2021

# importing pandas as pd
import pandas as pd
from pandas.core.frame import DataFrame

# reading csv data and storing it in variable data
print("\n\n\n\nAnswer 1:\nRaw Data")
data = pd.read_csv(
    "/Users/nikit/Desktop/Python/Lab/AircraftWildlifeIncident.csv")
# Answer1
print(data)
print("\n\n\n\n")

# cleaning data
# Answer2
print("Answer 2:")
print("Contains 'null' values: "+str(data.isnull().values.any())+"\nCleaned Data")
print(data.dropna())
print("\n\n\n\n")

# grouping data by country
# Answer3
print("Answer 3:\nGrouped by Incident Year Data")
newData = DataFrame(data.groupby("Incident Year").size())
newData.columns = ["No of Incidents"]
print(newData)
print("\n\n\n\n")

# Answer4
print("Answer 4:\nNo. of Incidents when the Species was 'MUNIAS': " +
      str(data[data['Species Name'] == 'MUNIAS']["Record ID"].count()))
