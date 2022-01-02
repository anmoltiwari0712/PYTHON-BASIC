#NOTE; THIS PROGRAM IS SAME AS THAT OF EXAMPLE 8.12 BUT THE OUTPUT PRODUCED IS DIFFERENT
#HENCE INDENTATION PLAYS MAJOR ROLE
sum=0
a=int(input("enter the ending number till which u need sum:"))
for n in range(1,a):
    sum=sum+n
print("sum of natural numbers <=",n,'is',sum)
