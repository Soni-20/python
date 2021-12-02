area_square=lambda side:side*side
area_rectangle=lambda length,width:length*width
area_triangle=lambda base,height:(base*height)/2
s=int(input("enter the side of square:"))
print("area of square",area_square(s))
l=int(input("enter the length of rectangle:"))
b=int(input("enter the breadth of rectangle:"))
print("area of rectangle",area_rectangle(l,b))
B=int(input("enter the base of triangle:"))
h=int(input("enter the height of triangle:"))
print("area of triangle",area_triangle(B,h))

