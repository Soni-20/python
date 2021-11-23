row1=int(input("enter the number"))
for i in range(0,row1+1):
        for j in range(i):
            print("*",end='')
        print("\n")
for i in range(row1-1,0,-1):
        for j in range(i):
            print("*",end='')
        print("\n")
