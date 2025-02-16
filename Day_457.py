
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

ny_zip = pd.read_csv('ny_zipcodes_split.txt')
ny_zip['NY_ZIPCODES'] = ny_zip['NY_ZIPCODES'].astype(str)

zip_shapes = gpd.read_file(r"D:\Downloads\tl_2023_us_zcta520\tl_2023_us_zcta520.shp")

merged = zip_shapes.merge(ny_zip, left_on='ZCTA5CE20',
                          right_on='NY_ZIPCODES')

merged.plot(column='DATA', legend=True)

plt.gca().axis('off')
plt.title('NY ZIP Code Data Visualization')
plt.show()

