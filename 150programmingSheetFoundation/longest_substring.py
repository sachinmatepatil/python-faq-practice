'''Problem Statement
Find the longest substring in a string that contains no repeating characters.
 Use sliding window or hash map techniques to efficiently find this substring.'''

'''
Example:
Input: "abcabcbb"
Output: "abc"

Input: "bbbbb"
Output: "b"
'''
s = "abcabcbb"
# Function to find the longest substring without repeating characters
def longest_substring(s):
    seen = {} # Empty dictionary to store the last index of each character
    left = 0
    long_sub_len = 0
    long_sub_start = 0

    for right in range(len(s)):
        ch = s[right]

        if ch in seen and seen[ch]>=left:
            left = seen[ch] + 1 # Move the left pointer to the right of the last occurrence of the character
        seen[ch] = right # Update the last index of the character

        # long_sub_len = max(long_sub_len, right - left + 1)
        curr_long_sub_len = right - left + 1

        if curr_long_sub_len > long_sub_len:
            long_sub_len = curr_long_sub_len
            long_sub_start = left

    return long_sub_len, s[long_sub_start:long_sub_start+long_sub_len]

# test the function

print(longest_substring(s))

#time complexity: O(n) where n is the length of the string, as we traverse the string once.
#space complexity: O(n) in the worst case, if all characters are unique, we store each character in the dictionary.
