# lst = [5,39,34,4,5,2,34,53,43]
# #Approach 1 using direct python method
# # lst.reverse()
# # print(lst)
#
# #Approach 2: using slicing
# reverse=lst[::-1]
# print(reverse)
#
nums = [1, 2, 310, 0, 123, 2, 4, 5]


def reverse_list(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums


print(reverse_list(nums))