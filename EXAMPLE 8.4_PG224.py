#TO TEST THE DIVISIBLITY OF TWO NUMBERS
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
remainder=num1%num2
if remainder==0:
    print(num1,"is divisible by",num2)
else:
        print(num1,"is not divisible by",num2)