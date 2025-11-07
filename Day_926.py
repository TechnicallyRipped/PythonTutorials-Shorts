

import xml.etree.ElementTree as ET

root = ET.Element("book")

title = ET.SubElement(root,"title")
title.text = "Python 101"
author = ET.SubElement(root,"author")
author.text = "TechnicallyRipped"

tree = ET.ElementTree(root)
tree.write("myFile.xml")

