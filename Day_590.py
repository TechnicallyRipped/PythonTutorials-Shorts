

# pip install python-box
from box import Box

x = {
    'Name' : 'John',
    'Age' : 30,
    'Location' : 'NY',
    'Last Name' : 'Johnson'
}

x2 = Box(x)

print(x2['Last Name'])



