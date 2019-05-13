import csv

with open("Sales Records.csv", "r") as old_csv:
    reader = csv.reader(old_csv)
    fruit_total = 0
    clothes_total = 0
    meat_total = 0
    beverages_total = 0
    office_supplies_total = 0
    cosmetics_total = 0
    snacks_total = 0
    personal_care_total = 0
    household_total = 0
    vegetables_total = 0
    baby_food_total = 0
    cereal_total = 0
    item_list = []
    for row in reader:
        if row[0] == 'Region':
            continue
        thing = row[13]
        # print(thing)
        item_type = row[2]
        if item_type not in item_list:
            item_list.append(item_type)
        if item_type == 'Fruits':
            fruit_total += float(thing)
        if item_type == 'Clothes':
            clothes_total += float(thing)
        if item_type == 'Meat':
            meat_total += float(thing)
        if item_type == 'Beverages':
            beverages_total += float(thing)
        if item_type == 'Office Supplies':
            office_supplies_total += float(thing)
        if item_type == 'Cosmetics':
            cosmetics_total += float(thing)
        if item_type == 'Snacks':
            snacks_total += float(thing)
        if item_type == 'Personal Care':
            personal_care_total += float(thing)
        if item_type == 'Household':
            household_total += float(thing)
        if item_type == 'Vegetables':
            vegetables_total += float(thing)
        if item_type == 'Baby Food':
            baby_food_total += float(thing)
        if item_type == 'Cereal':
            cereal_total += float(thing)
print(item_list)
print("Fruit Profit:", fruit_total)
print("Clothes Profit:", clothes_total)
print("Meat Profit:", meat_total)

