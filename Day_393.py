

# pip install geopy

from geopy.distance import great_circle

x = (40.7128, -74.0060)  # New York City
y = (34.0522, -118.2437)  # Los Angeles

distance = great_circle(x, y).miles
print(distance)

distance = great_circle(x, y).feet
print(distance)

distance = great_circle(x, y).kilometers
print(distance)

distance = great_circle(x, y).meters
print(distance)
