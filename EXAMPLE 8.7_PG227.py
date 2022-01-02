#TO READ TWO NUMERS AND GET INPUT OF A OPERATOR
num1=float(input("enter the first number:"))
num2=float(input("enetr the second number:"))
op=input("enter the operator of your choice[+ - * /]:")
if op=='+':
    sum=num1+num2
    print("the sum of two numbers is",sum)
elif op=='-':
    difference=num1-num2
    print("the difference of two numbers is",difference)
elif op=='*':
    product=num1*num2
    print("the product of two numbers is",product)
elif op=='/':
    remainder=num1/num2
    print("the remainder is",remainder)
else:
    print("invalid operator!!")
