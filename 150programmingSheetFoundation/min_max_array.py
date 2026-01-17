'''
Problem Statement
You stumble upon a list of magical stones, each with a power level. Your task is to find the most powerful and the weakest stone in the collection.

Examples
Input:
array = [4, 7, 1, 8, 5]
Output:
Largest: 8, Smallest: 1
Explanation:
The largest number in the array is 8 and the smallest is 1.
Input:
array = [10, 10, 10]
Output:
Largest: 10, Smallest: 10
Explanation:
All numbers are the same, so largest and smallest both are 10.
Input:
array = [-5, -2, -9, 0]
Output:
Largest: 0, Smallest: -9
Explanation:
Largest number is 0 and smallest number is -9.

'''

array = [4, 7, 1, 8, 5]

# array = [10,10,10]
# array = [-5,-2,-9,0]

# Method 1
# print(min(array))
# print(max(array))

# Method 2
# def min_max(array):
#     sort_list = sorted(array)
#     return sort_list[0],sort_list[-1]

# print(min_max(array))

# Method 3

def min_max(array):
    mins = maxs = array[0]

    for num in array:
        if num < mins:
          mins = num
        elif num > maxs:
            maxs = num

    return mins,maxs
print(min_max(array))

'''⏱️ Complexity (IMPORTANT)

Time Complexity
	•	One pass through array
	•	O(n) ✅ optimal

Space Complexity
	•	Only two variables
	•	O(1)

⸻

🎤 Interview One-Liner (Memorize)

I traverse the array once, updating minimum and maximum values, which gives an O(n) time and O(1) space solution.'''