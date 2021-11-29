
def arms(x):
    s=0
    z=x
    while(x!=0):
        r=int(x%10)
        x=int(x/10)
        s+=r**3
    if(s==z):
        print("number is srmstrong")
    else:
        print("number is not armstrong")
print("enter the number")
a=int(input())
arms(a)


    
