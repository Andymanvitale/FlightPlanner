import pandas as pd
# Import a CSV file to read the names of the airports
df = pd.read_csv('../all-airport-data.csv')
        
userInput1 = input("Departure airport Code: ")
userInput2 = input("Arrival airport code: ")
# Create a variable for lat/lon for airport 1 and 2
airport1 = df.iloc[userInput1]
# Read the CSV file to get store the lat/lon 

#Use GeoPy to calculate distance between the two airports