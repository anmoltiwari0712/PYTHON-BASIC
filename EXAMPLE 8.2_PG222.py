    #TO ACCEPT THREE NUMBERS AND PRINT THE LARGEST AMONG IT
x=int(input("enter the first number:"))
y=int(input("enter the second number:"))
z=int(input("enter the third number:"))
max=x
if y>max:
    max=y
if z>max:
    max=z
print("the largest number is",max)
