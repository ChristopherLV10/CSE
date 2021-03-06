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
    sub_saharan_africa_total = 0
    middle_east_and_north_africa_total = 0
    australia_and_oceania_total = 0
    europe_total = 0
    asia_total = 0
    central_america_and_the_caribbean_total = 0
    north_america_total = 0
    item_list = []
    region_list = []
    for row in reader:
        if row[0] == 'Region':
            continue
        thing = row[13]
        # print(thing)
        region = row[0]
        item_type = row[2]
        if item_type not in item_list:
            item_list.append(item_type)
        if region not in region_list:
            region_list.append(region)
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
        if region == 'Sub-Saharan Africa':
            sub_saharan_africa_total += float(thing)
        if region == 'Middle East and North Africa':
            middle_east_and_north_africa_total += float(thing)
        if region == 'Australia and Oceania':
            australia_and_oceania_total += float(thing)
        if region == 'Europe':
            europe_total += float(thing)
        if region == 'Asia':
            asia_total += float(thing)
        if region == 'Central America and the Caribbean':
            central_america_and_the_caribbean_total += float(thing)
        if region == 'North America':
            north_america_total += float(thing)
print(item_list)
print(region_list)
print("Fruit Profit:", fruit_total)
print("Clothes Profit:", clothes_total)
print("Meat Profit:", meat_total)
print("Beverages Profit:", beverages_total)
print("Office Supplies Profit:", office_supplies_total)
print("Cosmetics Profit:", cosmetics_total)
print("Snacks Profit:", snacks_total)
print("Personal Care Profit:", personal_care_total)
print("Household Profit:", household_total)
print("Vegetable Profit:", vegetables_total)
print("Baby Food Profit:", baby_food_total)
print("Cereal Profit:", cereal_total)
print("Sub-Saharan Africa Profit:", sub_saharan_africa_total)
print("Middle East and North Africa Profit:", middle_east_and_north_africa_total)
print("Australia and Oceania Profit:", australia_and_oceania_total)
print("Europe Profit:", europe_total)
print("Asia Profit:", asia_total)
print("Central America and the Caribbean Profit:", central_america_and_the_caribbean_total)
print("North America Profit:", north_america_total)


list_of_profits = [fruit_total, clothes_total, meat_total, beverages_total, office_supplies_total, cosmetics_total,
                   snacks_total, personal_care_total, household_total, vegetables_total, baby_food_total,
                   cereal_total]
list_of_items = ["Fruits", "Clothes", "Meat", "Beverages", "Office Supplies", "Cosmetics", "Snacks", "Personal Care",
                 "Household", "Vegetable", "Baby Food", "Cereal"]
index_of_item = list_of_profits.index(max(list_of_profits))
print("The most profit is", list_of_items[index_of_item], "at", max(list_of_profits))

list_of_regions = ['Sub-Saharan Africa', 'Middle East and North Africa', 'Australia and Oceania', 'Europe', 'Asia',
                   'Central America and the Caribbean', 'North America']
list_of_region_profits = [sub_saharan_africa_total, middle_east_and_north_africa_total, australia_and_oceania_total,
                          europe_total, asia_total, central_america_and_the_caribbean_total, north_america_total]
index_of_region = list_of_region_profits.index(max(list_of_region_profits))
print("The most profit is", list_of_regions[index_of_region], "at", max(list_of_region_profits))
