import csv

with open("name.csv","r") as csv_file:
    csv_reader=csv.reader(csv_file)

    for line in csv_reader:
        print(line[2])
