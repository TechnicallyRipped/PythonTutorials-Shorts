




#pip install geopy
from geopy.geocoders import Nominatim

address = "901 Cherry Avenue, San Bruno, CA"
geolocator = Nominatim(user_agent="address_geocoder")
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude

print(f"Latitude: {latitude}, Longitude: {longitude}")
























