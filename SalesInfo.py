import csv

with open("Sales Records.csv", "r") as old_csv:
    reader = csv.reader(old_csv)
    for row in reader:
        thing = row[13]
        print(thing)
