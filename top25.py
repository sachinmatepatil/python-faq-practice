 # 1 difference between list and tuple in python

lists = [1,2,3,4,5] #mutable
tuples = (1,2,3,4,5) #Immutable

# 2 What are pythons built-in data types?
#Numbers, Strings, dictionary, list, tuple, boolean, arithmetic, set, frozenset
# dicts = {'key':'values','name':'sachin','age':24}
# sets = (1,2,3,4,5)
# frozenset = frozenset((1,2,3,4,5))
# strings = 'sachin'
# booleans = True
# numb = 123
# arithmetic = 10 + 5
# list = [1,2,3,4,5]
# tuple = (1,2,3,4,5)

#How do you implement inheritance and super keyword in python?

#how to read and write a file in python?

with open('sample.txt','w') as f:
    f.write(str(lists))
    with open('sample.txt','r') as f:
        contents = f.read()



