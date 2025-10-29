lst = [1,3,2,3,5,12,2,4,3,5,4]
x=3
counter=0

#Method 1 using loop
# for i in lst:
#     if i==x:
#         counter=counter+1
# print(counter)

#Method 2: using count

# x=lst.count(3)
# print('found ',x)

#Method 2: using counter from collection package
# from collections import Counter
# dic=Counter(lst)
# print(dic)
# print(dic[3])