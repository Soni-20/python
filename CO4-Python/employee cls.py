class  employee :
   
    def __init__(self,a,num):
        self.__a=a;
        self.__num=num;
    def salary(self):
         self.s=self.__a*self.__num;
    def __lt__(self,other):
        if(self.s<other.s):
            return "obj1 is less than the obj2"
        else:
            return "obj1 is greater than the obj2"
print("enter the salary of 1st employee");
e1=int(input())
print("enter the number of working days of first employee");
d1=int(input())
print("enter the salary of  2nd employee");
e2=int(input())
print("enter the number of working days of 2nd employee");
d2=int(input())
s1=employee(e1,d1)
s2=employee(e2,d2)
s1.salary()
s2.salary()
print(s1<s2)
