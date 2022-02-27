a = open('txt1.txt', 'r')
  

b = open('sample.txt', 'w')
  

cont = a.readlines()
type(cont)
for i in range(0, len(cont)):
    if(i % 2 != 0):
        b.write(cont[i])
    else:
        pass
  

b.close()
  

b = open('sample.txt', 'r')
  

cont1 = b.read()
  

print(cont1)
  

a.close()
b.close()
