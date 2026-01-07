# arr = [3,123,34,3,23,234,23,53,45]
#
# #MEthod 1
# lst.sort()
# print(lst[-2])
#
# #MEthod 2
#
# myList = set(lst)
# myList.remove(max(myList))
# print(myList)
# print(max(myList))


# def second_max(arr):
#     if len(arr) < 2:
#         return None
#
#     first = second = float('-inf')
#
#     for num in arr:
#         if num > first:
#             second = first
#             first = num
#         elif first > num > second:
#             second = num
#
#     return second if second != float('-inf') else None
#
# print(second_max(arr))

#Conver string numbber to interger and sort it
str_nums = ['3', '123', '34', '3', '23', '234', '23', '53', '45']
int_nums = [int(num) for num in str_nums]
int_nums.sort()
print(int_nums)


#Method 2:

# x=sorted(map(int, list))
# print(x)


#Conver string number to interger and sort it based on the minutes place
#
# list = ["10:20","9:12","11:23","12:56:","09:14"]
#
# # x=list[0].split(':')
# new_list = []
# for num in list:
#     a = num.split(':')
#     new_list.append(a)


#Program to change uppercase to lowercase and vice versa
# s = 'Sachin Mate Patil'
#
# def strUpdate(s):
#     for c in s:
#         if c.isupper():
#             s = s.replace(c, c.lower())
#         elif c.islower():
#             s = s.replace(c, c.upper())
#     return s
#
# print(strUpdate(s))




# # int_nums = [int(num) for num in new_list]
# # print(int_nums)
# print(new_list)
# # kl = sorted(map(int,new_list))
# # print(kl)
# new_list.sort(key=lambda x:x[1] )
# print(new_list)


# Program to find the largest and second most frequent number in a list

lst = [3,123,34,3,23,234,23,53,45]

def find_most_freq_and_second_freq_num(lst):

    freq_dict = {}

    first_count = 0
    second_count = 0
    first_num = None
    second_num = None

    for num in lst:
        if num in freq_dict:
            freq_dict[num]+=1
        else:
            freq_dict[num]=1

    for num in freq_dict:
        if freq_dict[num] > first_count:
            second_count = first_count
            second_num = first_num

            first_count = freq_dict[num]
            first_num = num
        elif freq_dict[num] > second_count:
            second_count = freq_dict[num]
            second_num = num

    return first_num, second_num

print(find_most_freq_and_second_freq_num(lst))









