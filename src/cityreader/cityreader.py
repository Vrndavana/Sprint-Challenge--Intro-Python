import csv

cities = []

class City:
  def __init__(self, name,lat,lon):
    self.name = name
    self.lat = lat
    self.lon = lon

def cityreader(cities=[]):

  with open("cities.csv") as p:
    city_parser = csv.DictReader(p, delimiter= ",", quotechar = "|")
    for row in city_parser:
      city = City(row["city"], float(row["lat"]), float(row["lng"]))
      cities.append(city)

  # TODO Implement the functionality to read from the 'cities.csv' file
  # For each city record, create a new City instance and add it to the 
  # `cities` list
  # so call the csv function then  pass dth a tex tfile i want to iterate teham ti aute 
  #iterate the fucntion putting the for loop insife of the cities list.
    return cities
cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)
    print(c.name, c.lat, c.lon)