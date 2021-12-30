num=int(input("ENTER A NUMBER (0-999): "))
if num<0:
    print("INVALID ENTRY!!")
elif num<10:
    print("SINGLE DIGIT NUMBER IS ENTERED")
elif num<100:
    print("TWO DIGIT NUMBER IS ENTERED")
elif num<999:
    print("THREE DIGIT NUMBER IS ENTERED")
else:
    print("PLEASE ENTER A VALID NUMBER(0-999) ")
