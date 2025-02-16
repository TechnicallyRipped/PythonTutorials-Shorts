

import folium

pin1 = [34.0549,-118.2426]

my_map = folium.Map(location=pin1,
                    zoom_start=12)

folium.CircleMarker(location=pin1,
                    popup='PIN 1',
                    radius=100,
                    color='blue',
                    fill=True,
                    fill_color='green').add_to(my_map)


my_map.save("my_map3.html")





