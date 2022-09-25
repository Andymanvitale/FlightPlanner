import pandas as pd
import geopy as gp
# Import a CSV file to read the names of the airports
df = pd.read_csv('../all-airport-data.csv')
        
userInput1 = input("Departure airport Code: ")
userInput1.upper()
userInput2 = input("Arrival airport code: ")
# Create a variable for lat/lon for airport 1 and 2
latInput1 = df.ARPLatitude[df["LocId"] == userInput1]

longInput1 = df.ARPLongitude[df["LocId"] == userInput1]
#Change from DMS to decimal lat and longitude
rawStartLat = str(latInput1).split()
latValue = rawStartLat[1]
arrayLat = str(latValue).split("-")
startingPointLat = int(arrayLat[0]) + (int(arrayLat[1]) / 60) + (int(arrayLat[2][:2]) / 3600)
print(startingPointLat)
#Same for Longitude
rawStartLongitude = str(longInput1).split()
longValue = rawStartLongitude[1]
arrayLongitude = str(longValue).split("-")
startingPointLong = int(arrayLongitude[0]) + (int(arrayLongitude[1]) / 60) + (int(arrayLongitude[2][:2]) / 3600)
print(startingPointLong)
