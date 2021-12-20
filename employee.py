class Employee:
  def __init__(self, name, designation,salary):
    self.name = name
    self.designation = designation
    self.salary=salary
n=int(input("enter the number of employees"))
a=[]
for i in range(0,n):
    m=input("enter the name")
    q=input("enter the designation")
    s=input("enter the salary")
    e1=Employee(m,q,s)
    a.append(e1)
for i in range(0,n):
    print(a[i].name)
    print(a[i].designation)
    print(a[i].salary)
