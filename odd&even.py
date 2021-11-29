s=[1,2,3,4,5,6]
s1=[]
s2=[]
for i in s:
  if(i%2)==0:
      s1.append(i)
  else:
      s2.append(i)
print("even number is:",s1)
print("odd number is :",s2)
