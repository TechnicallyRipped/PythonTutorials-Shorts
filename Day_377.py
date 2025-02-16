

import pickle

# x = 10
# y = {'A' : 5}

# with open('my_data.pkl', 'wb') as f:
#     pickle.dump([x,y], f)

with open('my_data.pkl', 'rb') as f:
    data = pickle.load(f)

print(f'Loaded data: {data}')
print(data[0])
print(data[1])





























