#TO CALCULATE THE FACTORIAL OF A NUMBER
num=int(input("enter a number:"))
fact=1
a=1
while a<=num:
    fact=fact*a
    a=a+1
print("the factorial of",num,"is",fact)
