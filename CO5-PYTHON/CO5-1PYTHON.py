x = open("txt1.txt","r")
a=[]
for i in x.readlines():
    a.append(i.strip())
print(a)
