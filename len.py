print("enter the num of words")
x=int(input())
a=[]
for i in range(0,x):
    s=input()
    a.append(len(s))
print("length of longest word is",max(a))
