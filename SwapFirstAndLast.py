
# -----------------------------
# lst = [89,123,23,34,1,32,4]
# Approach 1
# temp = lst[0]
# lst[0] = lst[-1]
# lst[-1] = temp
# print(lst)

#Approach 2
# lst[0],lst[-1]=lst[-1],lst[0]
# print(lst)

#Approach 3 using tuple
# get=(lst[-1],lst[0]) #packing
# lst[0],lst[-1]=get
# print(lst)

#Approach 4 using * operand
# start,*middle,end=lst
# lst=[end,*middle,start]
# print(lst)

#Approach using pop
# first=lst.pop(0)
# last=lst.pop(-1)
# lst.insert(0,last)
# lst.append(first)
# print(lst)