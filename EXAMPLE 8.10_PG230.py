#TO PRINT THE ROOTS OF A QUADRATIC EQUATION
import math
print("for quadratic equation ax**2+bx+c,enter the coefficients of a,b,c below")
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
if a==0:
    print("value of a should not be zero")
    print("try re-entering the coefficients")
else:
    d=b**2-4*a*c
    if d>0:
        root1=(-b+math.sqrt(d))/(2*a)
        root2=(-b-math.sqrt(d))/(2*a)
        print("roots are real and unequal ")
        print("root1=",root1,"root2=",root2)
    elif d==0:
        root1=-b/(2*a)
        print("roots are real and equal")
    else:
        print("no roots exist")
