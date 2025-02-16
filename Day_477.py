

import folium

pin1 = [34.0549,-118.2426]
pin2 = [34.0549,-118.2226]

my_map = folium.Map(location=pin1,
                    zoom_start=12)

folium.Marker([pin1[0], pin1[1]],
               popup='PIN 1').add_to(my_map)

folium.Marker([pin2[0], pin2[1]],
               popup='PIN 2').add_to(my_map)

my_map.save("my_map2.html")





