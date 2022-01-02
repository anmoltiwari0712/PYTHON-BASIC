numbers=[2,3,4,5,6,7,8,4,2,6,5]
uniques=[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
