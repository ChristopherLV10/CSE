import csv

with open("Sales Records.csv", "r") as old_csv:
    reader = csv.reader(old_csv)
    fruit_total = 0
    for row in reader:
        thing = row[13]
        # print(thing)
        item_type = row[2]
        if item_type == 'Fruits':
            fruit_total += float(thing)
print(fruit_total)


