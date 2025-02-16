




import csv

with open('example_csv.csv') as file:
    content = csv.reader(file)
    for row in content:
        print(row[1])








