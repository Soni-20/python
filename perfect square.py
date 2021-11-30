import math
list1=[]
num=int(input("enter the string"))
if num>999:
    for i in range(1000,num):
        if i%2==0:
            root=math.sqrt(i)
            if int(root+.5)**2==i:
                list1.append(i)
print(list1)
