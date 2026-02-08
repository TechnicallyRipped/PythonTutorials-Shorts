


og_list = [1,2,3,4,5]

to_remove = [1,4]

x = list(filter(lambda x: x not in to_remove, og_list))

print(x)