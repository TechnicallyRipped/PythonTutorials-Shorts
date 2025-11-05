

import xml.etree.ElementTree as ET

tree = ET.parse("test_xml.xml")

root = tree.getroot()

for t1 in root:
    for t2 in t1:
        print(t2.text)


