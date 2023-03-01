name1 = input("name1: ")
age1 = input("age1: ")
name2 = input("name2: ")
age2 = input("age2: ")
name3 = input("name3: ")
age3 = input("age3: ")
mydict = {name1: age1, name2: age2, name3: age3}
# print(mydict)
if age1>age2>=age3:
    print(name1)
if age2>age1>=age3:
    print(name2)
if age3>age2>=age1:
    print(name3)
if age1==age2>age3:
    print(name1,"and",name2)
if age1==age3>age2:
    print(name1,"and",name3)
if age2==age3>age1:
    print(name2,"and",name3)
if age1==age2==age3:
    print("all the same age")