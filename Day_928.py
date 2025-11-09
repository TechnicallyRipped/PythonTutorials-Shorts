

import xml.etree.ElementTree as ET

tree = ET.parse("library.xml")

root = tree.getroot()

books = root.findall('book')

for book in books:
    price = book.find('price')
    book.remove(price)

tree.write("library_noPrice.xml")

