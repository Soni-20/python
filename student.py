class student:
    def _init_(self,name,roll):
     self.name=name
     self.roll=roll
n=int(input("enter the number of students")
a=[]
    for i in range(0,n):
          m=input("enter the name")
          q=input("enter the roll")
          p1=student(m,q)
          a.append(p1)
    for i in range(0,n):
          print(a[i].name)
          print(a[i].roll)
          
          
