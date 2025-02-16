



def num_count(_string):
    return sum(item.isdigit() for item in _string)

my_string = '52a'
print(num_count(my_string))