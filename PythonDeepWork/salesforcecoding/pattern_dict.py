#Pattern Dictionary(HashMap)

'''A dictionary lets you store:

item → count
item → last_seen_index
item → True/False


This helps you solve:
frequency problems
lookup problems
mapping problems
duplicate detection
anagram grouping'''
from RemoveNthOcc import count

#Template 1 - Count frequencies
# counts = {}
# for x in items:
#     counts[x] = counts.get(x, 0) + 1 #"Find the count for x. If you can't find x, pretend the count is 0. Then, add 1 to it and save the result.

#Template 2 - Find first unique
# def first_unique(s):
#     counts={}
#     for ch in s:
#         counts[ch] = counts.get(ch, 0) + 1
#
#     for ch in s:
#         if counts[ch] == 1:
#             return ch
#     return None

#Write a function to return the number of unique values in a list.
list = [1,2,2,3,3,3]
def uniq_values(list):
    count = {}
    for num in list:
        count[num] = count.get(num, 0) + 1
    return len(count)

print(uniq_values(list))

#Python trick
len(set(count)) #return the len of dic with uniq val
