import pandas as pd
from geopy import distance
from .models import airportModel
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()


def airports(code):
    if len(code) == 4 and code[0].upper() == "K":
        code = code[1:]
        return code
    return code


def findDistance():
    try:
        startApt = airports(airportModel.objects.values_list('startApt', flat = True).last())
        endApt = airports(airportModel.objects.values_list('endApt', flat = True).last())
        df = pd.read_csv('FlightPlanner/all-airport-data.csv')
        # Create a variable for lat/lon for airport 1
        latInput1 = df.ARPLatitude[df["LocId"] == startApt]
        longInput1 = df.ARPLongitude[df["LocId"] == startApt]

        #Change from DMS to decimal lat and longitude !!!STARTING!!!
        rawStartLat = str(latInput1).split()
        latValue = rawStartLat[1]
        arrayLat = str(latValue).split("-")
        startingPointLat = int(arrayLat[0]) + (int(arrayLat[1]) / 60) + (int(arrayLat[1][:2]) / 3600)
        

        #Changing DMS for Longitude !!!STARTING!!!
        rawStartLongitude = str(longInput1).split()
        longValue = rawStartLongitude[1]
        arrayLongitude = str(longValue).split("-")

        startingPointLong = int(arrayLongitude[0]) + (int(arrayLongitude[1]) / 60) + (int(arrayLongitude[2][:2]) / 3600)

        #If in the western hemisphere (Longitude is W) then multiply by -1 to be in the correct hemisphere
        if "W" in arrayLongitude[2]:
            startingPointLong *= -1

        #Create a variable for lat/lon !!!ENDING!!!
        latInput2 = df.ARPLatitude[df["LocId"] == endApt]
        longInput2 = df.ARPLongitude[df["LocId"] == endApt]

        #Change from DMS to decimal lat and longitude !!!ENDING!!!
        rawEndLat = str(latInput2).split()
        latEndValue = rawEndLat[1]
        arrayEndLat = str(latEndValue).split("-")
        endPointLat = int(arrayEndLat[0]) + (int(arrayEndLat[1]) / 60) + (int(arrayEndLat[2][:2]) / 3600)

        #Same for Longitude
        rawEndLongitude = str(longInput2).split()
        longEndValue = rawEndLongitude[1]
        arrayEndLongitude = str(longEndValue).split("-")
        endPointLong = int(arrayEndLongitude[0]) + (int(arrayEndLongitude[1]) / 60) + (int(arrayEndLongitude[2][:2]) / 3600)

        #If in the western hemisphere (Longitude is W) then multiply by -1 to be in the correct hemisphere
        if "W" in arrayEndLongitude[2]:
            endPointLong *= -1

        #Create start point as array for lat lon
        startTuple = (startingPointLat, startingPointLong)
        endTuple = (endPointLat, endPointLong)
        final = (distance.distance(startTuple, endTuple).nm)
        final = (str(round(final, 2)) + " NM")

        return final
    except:
        return "Invalid Airport Code"
        