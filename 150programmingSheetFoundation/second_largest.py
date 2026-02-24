'''
Problem Statement
Given an array, find the second largest number. Sorting the array or scanning twice can solve this. This is a classic problem testing array manipulation and sorting techniques.

Examples
Input:
array = [10, 20, 4, 45, 99]
Output:
45
'''

#Method 1: using in built sort and slicing
def second_largest(arr):
    if len(arr)<2:
        return None
    sorted_arr = sorted(arr)
    return sorted_arr[-2]

#example usage
arr = [10, 20, 4, 45, 99]
print(second_largest(arr))

#Method 2: using a single pass

def second_largest(arr):
    if len(arr)<2:
        return None

    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num

    if second == float('-inf'): #This means there was no second largest element (all elements are the same)
        return None

    return second

#example usage
arr = [10, 20, 4, 45, 99,896]
print(second_largest(arr))

'''
⏱ Complexity
	•	Time Complexity: O(n)
	•	Space Complexity: O(1)
'''