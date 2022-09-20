import pandas as pd
# Import a CSV file to read the names of the airports
df = pd.read_csv('../all-airport-data.csv')
        
userInput1 = input("Departure airport Code: ")
userInput1.upper()
userInput2 = input("Arrival airport code: ")
# Create a variable for lat/lon for airport 1 and 2
latInput1 = df.ARPLatitude[df["LocId"] == userInput1]
longInput1 = df.ARPLongitude[df["LocId"] == userInput1]
print(latInput1)
print(longInput1)
# Read the CSV file to get store the lat/lon 
# print(df.ARPLatitude + ' ' + df.ARPLongitude)
#Use GeoPy to calculate distance between the two airports