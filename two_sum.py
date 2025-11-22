# Problem: Given an array and a target,
# return indices of two numbers that add up to the target.

# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.

nums = [2,3,7,11,15]
target = 13

#Method 1: using for loop - This is two loops, O(n²). Works—but slow.
# for i in nums:
#     for j in nums:
#         if i + j == target and i != j:
#             print(nums.index(i),nums.index(j))
#             break

#Method 2 - using dictionary - this is 0(n) faster

def two_sum(nums, target):
    dict = {} # Empty dict to store number and index
    for i,num in enumerate(nums): #for every number in the list,give me two things: the index i and the number num.”
        # print(dict)
        # print(i)
        # print(num)
        needed = target - num #What number do we need to complete target

        if needed in dict: # is O(1) — constant time.So entire solution runs in O(n) — best possible.
            return [dict[needed], i]

        dict[num] = i #Store number with its index
    return None

print(two_sum(nums, target))


#What enumerate does
#
# enumerate(nums) turns this:
#
# [10, 20, 30, 40]
#
#
# into this:
#
# (0, 10)
# (1, 20)
# (2, 30)
# (3, 40)
#
#
# Each item becomes a pair:
#
# first = index
#
# second = value


