import csv


def validate(num: str):
    if not all_16_degits(num):
        return False
    if divisible_by_2(num) and divisible_by_3(num):
        return True
    return False


def divisible_by_3(num: str):
    first_num = int(num[0])
    if first_num % 3 == 0:
        return True
    return False


def divisible_by_2(num: str):
    first_num = int(num[0])
    if first_num % 2 == 0:
        return True
    return False

def all_16_digits(num: str):



with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        print("Writing file...  ")
        writer = csv.writer(new_csv)
        reader = csv.reader(old_csv)
        print("Processing...")

    for row in reader:
        old_number = row[0]
        first_num = int(old_number[0])
        if validate(old_number):
            writer.writerow(row)
print("Done")
