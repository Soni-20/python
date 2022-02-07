import csv
a = []
with open('name.csv') as file:
    obj = csv.reader(file)

    for rows in obj:
       a.append(rows)

print(a)
