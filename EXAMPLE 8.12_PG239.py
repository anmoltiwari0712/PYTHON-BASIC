#TO PRINT THE SUM OF NUMBERS
#NOTE; THIS PROGRAM IS SLIGHTLY DIFFERENT FROM THE ONE IN BOOK
sum=0
a=int(input("enter the ending number till which u need sum:"))
for n in range(1,a):
    sum=sum+n
    print("sum of natural numbers <=",n,'is',sum)
