lst = [7, 93, 4, 3, 3, 123, 4, 5, 3, 4]

number = 5000
flag=0
# for i in lst:
#     if (i==number):
#         print('found')
#         flag=1
#         break
# if(flag==0):
#     print('E not found')

#Approach 2 : using in operator
if(number in lst):
    print('found')
else:
    print('not found')