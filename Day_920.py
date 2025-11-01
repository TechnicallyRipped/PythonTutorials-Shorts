

import pandas as pd

df = pd.read_csv('vehicles.csv')

vehicle_type = {'A':'Car',
                'B':'Truck',
                'C':'Motorcycle'}

df['Decode'] = df['Vehicle_Code'].map(vehicle_type)

print(df)














