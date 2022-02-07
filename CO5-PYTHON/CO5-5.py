import csv 
dict = [
{"name":"tessy","age":21,"roll no":"134"},
{"name":"kevin","age":21,"roll no":"135"},
{"name":"ancy","age":21,"roll no":"136"},
]

field = ["name","age","roll no"]

with open('dictconverted.csv','r+') as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames=field)
    writer.writeheader()
    writer.writerows(dict)
    csvfile.close()

with open('dictconverted.csv','r') as csvfiles:
    obj = csv.reader(csvfiles)
    for rows in obj:
        print(rows)
