


from itertools import chain

list_1 = [1,2,3]
tuple_1 = ("a","b","c")
string_1 = "HELLO"

chained = chain(list_1,tuple_1,string_1)

print(chained)

for item in chained:
    print(item)


