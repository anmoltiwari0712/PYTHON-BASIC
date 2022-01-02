#TO GET AN INPUT OF CHOICE TO FURTHER PROCEED THE PROGRAM
radius=int(input("enter radius of circle:"))
print("1.calculate its area")
print("2.calculate perimeter")
choice=int(input("enter your choice (1)or(2):"))
if choice==1:
    area=3.14159*radius*radius
    print("the area of the circle is",area) 
elif choice==2:
    perimeter=2*3.14159*radius
    print("the perimeter of the circle is",perimeter)
else:
    print("please enter your choice again")    
