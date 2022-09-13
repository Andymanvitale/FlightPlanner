import csv
# Import a CSV file to read the names of the airports
with open('../all-airport-data.csv', newline ='') as airportcsv:
    airportread = csv.reader(airportcsv, delimiter=' ')
    for row in airportread:
        print(' '.join(row))
        

# Create a variable for lat/lon for airport 1 and 2

# Read the CSV file to get store the lat/lon 

#Use GeoPy to calculate distance between the two airports