print("jan,feb,march,april,may,june,july,aug,sept,oct,nov,dec")
month=input("input name of month")
if month==("feb"):
    print("no of days:28/29")
elif("april","june","sept","nov"):
    print("no of days:30")
elif("jan","march","may","july","aug","oct","dec"):
    print("no of days:31")
else:
    print("wrong month name")
