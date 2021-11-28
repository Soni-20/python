print("enter the no:names")
n=int(input())
print("enter the names")
s=[]
c=0
for i in range(0,n):
    l=input()
    s.append(l)
    c+=l.count("a")
print("the count is:"c)
