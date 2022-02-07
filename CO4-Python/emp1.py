class  employee:
   def __init__(self,name,salary):
        self.name=name;
        self.salary=salary;
class  work :
    def __init__(self,name,days):
        self.name=name;
        self.days=days;
    def __mul__(self,other):
            return self.days*other.salary;
e=employee("ram",1000)
d=work("ram",30)
print(d*e)
