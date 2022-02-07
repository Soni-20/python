class  time :
    def __init__(self,hour,minute,second):
        self.__hour=hour;
        self.__minute=minute;
        self.__second=second;
    def __add__(self,other):
        h=self.__hour+other.__hour
        m=self.__minute+other.__minute
        s=self.__second+other.__second
        return str(h)+":"+str(m)+":"+str(s)
print("Enter first Time")
print("hrs");
h1=int(input())
print("mins");
m1=int(input())
print("sec");
s1=int(input())
print("Enter second Time")
print("hrs");
h2=int(input())
print("mins");
m2=int(input())
print("sec");
s2=int(input())
t1=time(h1,m1,s1)
t2=time(h2,m2,s2)
print(t1+t2)
