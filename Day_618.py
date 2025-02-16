
import pickle

# x = {'A': 1, 'B': 2, 'C': 3}
# y = [1, 2, 3, 4, 5]

# with open('test_data.pkl', 'wb') as file:
#     pickle.dump({'x': x, 'y': y},file)

with open('test_data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
    # print(loaded_data)
    x = loaded_data['x']
    y = loaded_data['y']
    print(f'{x=}, {y=}')















