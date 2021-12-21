class Student:
  def __init__(self,name,roll,phy,chem,maths,u,percent,avg):
    self.name = name
    self.roll = roll
    self.phy=phy
    self.chem=chem
    self.maths=maths
    self.u=u
    self.percent=percent
    self.avg=avg
n=int(input("enter the number of students"))
a=[]
for i in range(0,n):
    m=input("enter the name")
    q=input("enter the roll")
    h=int(input("enter the phy mark"))
    c=int(input("enter the chem mark"))
    t=int(input("enter the maths mark"))
    avg=(h+c+t)/3
    s=h+c+t
    g=(s*100)/300
    s1=Student(m,q,h,c,t,g,s,avg)
    a.append(s1)
for i in range(0,n):
    print(a[i].name)
    print(a[i].roll)
    print(a[i].phy)
    print(a[i].chem)
    print(a[i].maths)
    print(a[i].percent)
    print(a[i].avg)
    
