class Student:
  def __init__(self, name,roll,phy,chem,maths):
    self.name = name
    self.roll = roll
    self.phy=phy
    self.chem=chem
    self.maths=maths
    self.sum=sum
    self.percentage=percentage
n=int(input("enter the number of students"))
a=[]
for i in range(0,n):
    m=input("enter the name")
    q=input("enter the roll")
    h=input("enter the phy")
    c=input("enter the chem")
    t=input("enter the maths")
    u=input("enter the sum")
    g=input("enter the percentage")
    for i in range(0,n):
        s=h+c+m
        g=(s*100)/300
    s1=Student(m,q,h,c,t,g,s)
    a.append(s1)
for i in range(0,n):
    print(a[i].name)
    print(a[i].roll)
    print(a[i].phy)
    print(a[i].chem)
    print(a[i].maths)
    print(a[i].percentage)
