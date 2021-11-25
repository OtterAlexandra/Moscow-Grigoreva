import csv

with open('name.csv', mode='r', encoding="utf8") as csv_file:
    reader = csv.reader(csv_file, delimiter='')

    header = next(reader)

    for row in reader:
        print(row)

with open('name.csv', mode='w', encoding="utf8") as csv_file:
    reader = csv.writer(csv_file, delimiter='')