

# pip install xmltodict
import xmltodict
import json

with open("library.xml", "r") as file:
    xml_data = file.read()
    print(xml_data)

data_dict = xmltodict.parse(xml_data)

json_data = json.dumps(data_dict, indent=4)

with open("library.json", "w") as json_file:
    json_file.write(json_data)
