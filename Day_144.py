




from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="technicallyripped")

latitude = 37.628145950000004
longitude = -122.4264270211096

location = geolocator.reverse((latitude, longitude), 
                              exactly_one=True)

address = location.address

print(address)































