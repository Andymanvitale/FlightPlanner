import pandas as pd
from geopy import distance
from .models import airportModel


def findDistance(startApt, endApt):
    startApt = airportModel.objects.values('startApt')
    endApt = airportModel.objects.values('endApt')


    # Import a CSV file to read the names of the airports
    df = pd.read_csv('./all-airport-data.csv')
            
    userInput1 = startApt
    userInput2 = endApt
    # Create a variable for lat/lon for airport 1
    latInput1 = df.ARPLatitude[df["LocId"] == userInput1.upper()]
    longInput1 = df.ARPLongitude[df["LocId"] == userInput1.upper()]

    #Change from DMS to decimal lat and longitude
    rawStartLat = str(latInput1).split()
    latValue = rawStartLat[1]
    arrayLat = str(latValue).split("-")
    startingPointLat = int(arrayLat[0]) + (int(arrayLat[1]) / 60) + (int(arrayLat[2][:2]) / 3600)
    #print("Starting Lat: " + str(startingPointLat))

    #Same for Longitude
    rawStartLongitude = str(longInput1).split()
    longValue = rawStartLongitude[1]
    arrayLongitude = str(longValue).split("-")
    startingPointLong = int(arrayLongitude[0]) + (int(arrayLongitude[1]) / 60) + (int(arrayLongitude[2][:2]) / 3600)
    #print("Starting Long: " + str(startingPointLong))

    #If in the western hemisphere (Longitude is W) then multiply by -1 to be in the correct hemisphere
    if "W" in arrayLongitude[2]:
        startingPointLong *= -1

    #Create a variable for lat/lon for airport 2
    latInput2 = df.ARPLatitude[df["LocId"] == userInput2]
    longInput2 = df.ARPLongitude[df["LocId"] == userInput2]

    #Change from DMS to decimal lat and longitude
    rawEndLat = str(latInput2).split()
    latEndValue = rawEndLat[1]
    arrayEndLat = str(latEndValue).split("-")
    endPointLat = int(arrayEndLat[0]) + (int(arrayEndLat[1]) / 60) + (int(arrayEndLat[2][:2]) / 3600)
    #print("End Lat: " + str(endPointLat))

    #Same for Longitude
    rawEndLongitude = str(longInput2).split()
    longEndValue = rawEndLongitude[1]
    arrayEndLongitude = str(longEndValue).split("-")
    endPointLong = int(arrayEndLongitude[0]) + (int(arrayEndLongitude[1]) / 60) + (int(arrayEndLongitude[2][:2]) / 3600)
    #print("End Longitude: " + str(endPointLong))

    #If in the western hemisphere (Longitude is W) then multiply by -1 to be in the correct hemisphere
    if "W" in arrayEndLongitude[2]:
        endPointLong *= -1

    #Create start point as array for lat lon
    startTuple = (startingPointLat, startingPointLong)
    endTuple = (endPointLat, endPointLong)
    final = distance.distance(startTuple, endTuple).nm
    return final

    
   # def distance():
    #    distance = (distance.distance(startTuple, endTuple).nm)
   #     return render(distance, 'index.html')
