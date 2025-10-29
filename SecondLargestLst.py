lst = [3,123,34,3,23,234,23,53,45]

#MEthod 1
lst.sort()
print(lst[-2])

#MEthod 2

myList = set(lst)
myList.remove(max(myList))
print(myList)
print(max(myList))