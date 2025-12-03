"""Two Pointers: using two indexes to move through a list/string"""

'''You use this when:
You need to scan from left and right
You need to track two positions
You want to solve things faster than O(n²)

Examples it solves:
Reverse a list/string
Check if palindrome
Remove duplicates
Move zeroes
Merge sorted arrays
Pair sum in sorted array

Most common interview pattern'''

#Problem : Reverse the list [1,2,3,4] -> [4,3,2,1]
# l = [1,2,3,4,5,6]
# def reverse_list(l):
#     left, right = 0, len(l)-1
#
#     while left<right:
#         l[left], l[right] = l[right], l[left]
#         left +=1
#         right -=1
#     return l
# print(reverse_list(l))

#Example 2 - check if a string is a palindrome

# def is_palindrome(s):
#     left, right = 0 , len(s)-1
#
#     while left<right:
#         if s[left] != s[right]:
#             return False
#         left +=1
#         right -=1
#     return True
#
# st = ['sachin','level','madam','hello']
# for i in st:
#     print(is_palindrome(i))


#Example 3 move zeroes to the end
#Problem [0,1,0,3,12] -> [1,3,12,0,0]


def zeroends(l):
    pos = 0

    for i in range(len(l)):
        if l[i] != 0:
            l[pos], l[i] = l[i], l[pos]
            pos +=1

    return l
print(zeroends([1,2,3,4,0,5,6,7,0,8,9]))

#Find two number that sum to target

def two_sum(nums, target):
    left, right = 0, len(nums)-1

    while left<right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            # return [left, right]
            return [nums[left], nums[right]]
        elif current_sum < target:
            left +=1
        else:
            right -=1
    return []
print(two_sum([1,2,3,4,5,6,7,8,9], 9))

#Given a string, return it reversed

def reverse_string(s):
    char = list(s)
    left, right = 0 , len(char)-1

    while left<right:
        char[left], char[right] = char[right], char[left]
        left +=1
        right -=1
    return ''.join(char)
print(reverse_string('sachin'))