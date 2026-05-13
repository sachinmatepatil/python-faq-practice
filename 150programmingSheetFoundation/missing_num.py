# Missing Number: Find the missing number in an array of contiguous integers.

nums = [1, 2, 4, 5, 6]

def missing_num(nums):
    n = len(nums) + 1

    expected_sum = (min(nums) + max(nums)) * n // 2
    actual_sum = sum(nums)

    return expected_sum - actual_sum
print(missing_num(nums))

#Time complexity is O(n) because we need to calculate the sum of the numbers in the array, which takes O(n) time. The rest of the operations (calculating expected sum and returning the result) take constant time O(1). Therefore, the overall time complexity is O(n).
#Space complexity is O(1) because we are using a constant amount of extra space to store the expected sum and actual sum. We are not using any additional data structures that grow with the input size, so the space complexity is constant.


# If sequence is from 0 to n
def missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum