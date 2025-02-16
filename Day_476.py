

import folium

# Geolocation of Los Angeles
pin = [34.0549,-118.2426]

my_map = folium.Map(location=pin,
                    zoom_start=12)

folium.Marker([pin[0], pin[1]],
               popup='Los Angeles').add_to(my_map)

my_map.save("my_map.html")

