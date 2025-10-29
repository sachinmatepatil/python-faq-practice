lst = [1,3,324,45,7,5,4,6,4]
print(lst)
# lst.clear() #Approach 1
# print(lst)

#Approach 2: initializes the list with no value

# lst=[]
# print(lst)

#Approach 3: using *= operand
# lst *=0 #deletes the list
# print(lst)

#Approach 4: using del
del lst[:]
print(lst)