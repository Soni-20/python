class Rectangle:
  def __init__(self,name,length,breadth,perimeter,area):
    self.name=name
    self.length = length
    self.breadth = breadth
    self.area=area
    self.perimeter=perimeter
n=int(input("enter the number of rectangle"))
a=[]
for i in range(0,n):
    m=input("enter the nameof rectangle:")
    l=int(input("enter the length of rectangle:"))
    b=int(input("enter the breadth of rectangle:"))
    area=l*b
    perimeter=2*(l+b)
    r1=Rectangle(m,l,b,perimeter,area)
    a.append(r1)
for i in range(0,n):
    print(a[i].name,"has",)
    print("area:",a[i].area)
    print("perimeter:",a[i].perimeter)
for i in range(0,n-1):
    if(a[i].area>a[i+1].area):
        print("area of first rectangle is greater")
    else:
        print("area of second rectangle is greater")
    
    
