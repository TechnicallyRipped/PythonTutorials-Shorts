

import xml.etree.ElementTree as ET

tree = ET.parse("library.xml")

root = tree.getroot()

books = root.findall('book')

for book in books:
    title = book.find('title')
    print(title.text)

