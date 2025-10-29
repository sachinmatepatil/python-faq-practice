#Approach 1: simple swap

lst = [23,65,19,90]

# pos1,pos2=1,3
# lst[pos1],lst[pos2]=lst[pos2],lst[pos1]
# print(lst)

#Approach 2 using pop
# pos1=lst.pop(1)
# pos2=lst.pop(2)
# lst.insert(1,pos2)
# lst.append(pos1)
# print(lst)

#Approach 3: using tuple
# get=(lst[1],lst[3])
# lst[3],lst[1]=get
# print(lst)