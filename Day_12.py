

list_1 = ['apple', 'banana', 'orange', 'pear']
list_2 = ['banana', 'strawberry', 'pear', 'blueberry']
count = 0

for item_1 in list_1:
    for item_2 in list_2:
        if item_1 == item_2:
            count += 1
        print(item_1, item_2)
        
print(count)








