


from itertools import chain

list1 = [1,2,3]
list2 = [4,5,6]
string1 = 'abc'

for item in chain(list1,list2,string1):
    print(item)