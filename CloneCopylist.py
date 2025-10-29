lst = [4,6,5,3,234,5,2]

# #MEthod 1 slicing
# lst_copy=lst[:]
# print(lst_copy)

#Method 2 using extend() method
# lst_copy=[]
# lst_copy.extend(lst)
# print(lst_copy)

#MEthod 3: using the list() method
# lst_copy = list(lst)
# print(lst_copy)

#Method 4: using the copy() method
# lst_copy = lst.copy()
# print(lst_copy)

#Method 5: using list comprehension
lst_copy=[i for i in lst]
print(lst_copy)