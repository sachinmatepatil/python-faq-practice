'''
A chaotic set of scrolls needs to be organized in increasing order of their magic levels. Help the wizard sort this array of numbers in ascending order.



Examples

Input:

array = [3, 1, 4, 1, 5, 9]
'''

def sort_array(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


array = [3, 1, 4, 1, 5, 9]
print(sort_array(array))

# What this code is doing (Brief Explanation)
# 	•	You assume the first element is already sorted
# 	•	You pick the next element (key)
# 	•	You shift larger elements to the right
# 	•	You insert key into its correct position
# 	•	Repeat until the array is sorted

'''⏱️ Complexity (Single-Line, Interview Style)
	•	Time Complexity: O(n²) worst case, O(n) best case (already sorted)
	•	Space Complexity: O(1) (in-place)

⸻

🎤 Interview One-Liner

I used insertion sort, which builds the sorted array incrementally by inserting each element into its correct position using constant extra space.'''
