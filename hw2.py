FirstName=input()
LasttName=input()
age=int(input())
DateofBirth=input()
 

lst=[]
lst.append(FirstName)
lst.append(LasttName)
lst.append(age)
lst.append(DateofBirth)

for i in lst: 
    print(i)

if age < 18:
    print("You cant go out because it's too dangerous")
elif age > 18:
    print("You can go out the street")