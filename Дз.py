import csv
from sys import stdin

with open('sea_rates.csv', mode='r', encoding="utf8") as csv_file:
    reader = csv.reader(csv_file, delimiter=',')

    begin = input().split()

    for i in reader:
        if i[0] == begin[0]:
            beg = i
        elif i[0] == begin[1]:
            end = i

latitude = abs(int(beg[1]) - int(end[1]))
longitude = abs(int(beg[2]) - int(end[2]))

print(latitude)
print(longitude)
