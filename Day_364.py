


my_list = ['tech','ripped']
values = ['like','subscribe']

for i,item in enumerate(my_list):
    globals()[item] = values[i]

# print(tech)
# print(ripped)

print(globals())













