#GeoLiteCity-Location.csv
import csv
from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r


original = file('GeoLiteCity-Location.csv', 'rU')
reader = csv.reader(original)
cities = {}

print "Loading Please Wait .... \n\n\n\n"

for rows in reader:
#    #will print each row by itself (all columns from names up to what they wear)
     #print row[5]
     cities[ rows[3] ] = {'Latitude':rows[5],'Longitude':rows[6] }
#    print "--------------------------------------------------------------------------"
#    #will print first column (character names only)
#    print row[0]



print "\t\tWelcome to Smart City Search \n\n "
name = raw_input("Please Enter City Name:")
print "City Latitude :", cities[name]["Latitude"]
print "City Longitude :", cities[name]["Longitude"]

print "Enter a City name to find nearby cities:"
name1 = raw_input("Please Enter 1st City Name:")
print "City Latitude :", cities[name1]["Latitude"]
print "City Longitude :", cities[name1]["Longitude"]

for c in cities:
    print "Distance" , haversine(float(cities[name1]["Longitude"]), float(cities[name1]["Latitude"]), 5.0, 51.0)



    


