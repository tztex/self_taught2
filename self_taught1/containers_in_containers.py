# list to tuple

names = ["Tom", "Jim", "Bill"]
team = ["jets", "cowboys", "raiders"]
namteam = (names, team)
print(namteam)
print(namteam[1])

#mapping key value pair is called mapping
# key values and maps with tuples( ) are immutable,
# list[ ] are interable and mutable
# and dictionaries { } ford_city is dictionary
ford_city = {"location":
                 (40.769450,
                  -79.530860),
             "friends":
             ["Scott", "Bill", "Ted", "Tom"],
             "facts":
                 {"state": "PA",
                  "country": "America"}
             }
print(ford_city)
print(type(ford_city))
print("friends" in ford_city)
print(ford_city["location"])
ford_city["founded"] = 1776
print(ford_city)
print(ford_city["facts"])
del ford_city["facts"]
print((ford_city))

#tuple list example
locations = [(40.7128, 74.0059), (31.0461, 34.8516), (8.3405, 115.0920)]
print(locations[0])
locations.pop() #remove last item in list
print(locations)
print(type(locations))
locations[0] = (111111,222222)
print(locations)
locations.append((333333,555555))
print(locations)





