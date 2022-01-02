#TO CHECK WHETHER THE ENTERED CHARACTER IS UPPERCASE OR LOWER CASE
ch=input("enter your single character:")
if ch>='A' and ch<='Z':
    print("you have entered an uppercase character")
elif ch>='a' and ch<='z':
    print("you have entered an lowercase character")
elif ch>='0' and ch<='9':
    print("you have entered a digit")
else:
    print("you have entered a special character")
