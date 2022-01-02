#PROGRAM TO IMPLEMENT GUESS THE NUMBER GAME
import random
a=int(input("enter the starting number:"))
b=int(input("enter the ending number:"))
number=random.randint(a,b)
ctr=0
while ctr<5:
    guess=int(input("now guess a number:"))
    if guess==number:
        print("you win!!!!!")
        break
    else:
        ctr=ctr+1
if not ctr<5:
    print("oops!!! you lose, the number was",number)
    
