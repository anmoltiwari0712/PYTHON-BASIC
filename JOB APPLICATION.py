
name=(input("enter your name:"))
print("hello",name,"nice to meet you!!!")
print("please fill the following details asked below to check your eligiblity.")
age=int(input("enter your age:"))
gender=(input("enter your gender:"))
if age<=18:
   print("!!!sorry you are not eligible for this job")
   print("program over")
else:
    grade=int(input("enter your 10th marks:"))
if grade>500:
   print("please enter your marks out of 500!!!")
else:
    if grade>450:
       print("wow!you have scored amazing marks in 10th")
if grade>350:
    print("good!it shows you have tried your best in 10th")
else:
    print("your score is not enough to apply for this job!!BETTER LUCK NEXT TIME")
if grade>450:
   print("congrats!!!you have been considered as eligible by us for this job")
   no=int(input("enter your no:"))
print("thanks for submitting all the details to us.")
print("our team will contact you shortly!!!!")
print("good bye")
              

    
    
