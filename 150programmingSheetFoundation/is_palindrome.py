# You want to verify if a given string reads the same backward as forward — a palindrome. To do this, you decide to write a program that compares characters from both ends moving towards the center, confirming if the string qualifies as a palindrome.

def is_palindrome(s):
    left , right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]: #compare characters
            return False
        left += 1
        right -= 1
    return True
# Example usage:
test_string = "racecar"
if is_palindrome(test_string):
    print(f'"{test_string}" is a palindrome.')
else:
    print(f'"{test_string}" is not a palindrome.')

'''I use two pointers starting from both ends and compare characters while moving inward. 
If all pairs match, the string is a palindrome.'''
''' Why This Approach Is Optimal
	•	Each character is checked once
	•	No extra memory used
	•	Stops early if mismatch found

Complexity:
	•	Time: O(n)
	•	Space: O(1)'''

''' Time Complexity: O(n)
	•	Let n be the length of the string.
	•	Two pointers start at:
	•	left = 0
	•	right = n - 1
	•	In each iteration:
	•	One comparison is made
	•	left moves right
	•	right moves left
	•	The loop runs until left < right, which is about n/2 comparisons.

📌 In Big-O notation:
	•	Constants are ignored → O(n)

👉 Each character is checked at most once.

⸻

💾 Space Complexity: O(1)
	•	Only a constant number of variables are used:
	•	left
	•	right
	•	No extra arrays, strings, stacks, or recursion.

👉 Space does not depend on input size.'''

'''Interview One-Liner (Use This)

The palindrome check runs in O(n) time since each character is compared once, and O(1) space because only two pointers are used.'''