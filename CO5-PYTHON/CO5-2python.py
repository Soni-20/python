x = open("txt1.txt","r")
c= open("sample.txt","w")
z=1
for i in x:
    if z%2!=0:
        c.write(i)
    z=z+1
c.close()
x.close()
