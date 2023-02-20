set1 = {1,2,3,4,5,6,7,8,9,10}
list1 = list(set1)
list1.remove(3)
list1.remove(5)
list1.remove(9)
list1.remove(10)
list1.insert(0,5)
list1.insert(1,4)
list1.insert(2,6)
list1.insert(3,7)
print(list1)
print(list1[3:6])
set1 = set(list1)
print(set1)
del set1
del list1
string1 = "this is the 3rd session homework"
string1split = string1.split()
print(string1split)
