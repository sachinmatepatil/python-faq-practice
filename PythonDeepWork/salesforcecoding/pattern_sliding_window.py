'''Sliding window mindset(the only 3 cases)

Case 1: Window size is fixed
Example : subarray sum of size k
-> window grows to size k
-> then slides forward by removing left element and adding right element

Use this when exact window size is known,given

Problem 1: Maximum sum of subarray of size k
input = arr = [2,1,5,1,3,2], k = 3
output = 9(subarray = [5,1,3])
'''


def max_sum_arr(arr,k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k,len(arr)):
        window_sum+=arr[i]
        window_sum-=arr[i-k]
        max_sum = max(max_sum,window_sum)
    return max_sum


arr = [2,1,5,1,3,2]
k = 3
print(max_sum_arr(arr,k))

#========================================
#=======================================
'''Case 2 : Window size is variable,Dynamic, this condition must be true
Example - longest substring without repeating characters
-> expand the window until condition breaks
-> shrink left side until condition becomes valid again

Use this when :
- longest substring
- shortest substring
- no duplicates
- sum less than X
- count < X
'''

#Longest Substring Without Repeating Characters

def longest_substring(s):
    seen = {}
    left = 0
    long_sub = 0

    for right in range(len(s)):
        ch = s[right]

        if ch in seen and seen[ch] >=left:
            left = seen[ch] + 1
        seen[ch] = right

        long_sub = max(long_sub, right - left + 1)
    return long_sub

print(longest_substring("abcasdfsdabcbb"))

'''I use a sliding window that expands with the right pointer.
When a duplicate character appears inside the window, I move the left pointer to one position after its last occurrence to maintain a valid window.
I track the maximum window size throughout.'''

#=======================================================
#====================================================

'''CASE 3 — Greedy window reset (used in your Hackerrank test)

Example: your valid subarray count problem
→ expand window
→ when condition met, count it and reset window
→ do not shrink

This is used rarely but VERY helpful.'''


# 🔑 KEY IDEA
#
# We are NOT finding longest/shortest window
#
# We are counting maximum number of valid non-overlapping windows
#
# Once a valid window is found → we TAKE it and RESET
#
# 👉 This is why it’s called greedy
'''🎯 Problem (Same pattern as your test)
Maximum number of valid subarrays

Conditions:

subarray length ≥ minLen

subarray sum ≥ threshold

subarrays must NOT overlap

Example:'''

def max_valid_subarrays(arr, minLen, threshold):
    curr_window_sum = 0
    left = 0
    count = 0

    for right in range(len(arr)):
        curr_window_sum+=arr[right]

        if (right - left+1) >=minLen and curr_window_sum >= threshold:
            count +=1
            left = right + 1
            curr_window_sum = 0

    return count

arr = [5, 3, 2, 5, 3, 2, 4]
minLen = 2
threshold = 7
print(max_valid_subarrays(arr, minLen, threshold))

'''Since subarrays must not overlap, I use a greedy sliding window.
The moment the window satisfies the length and sum conditions, I count it and reset the window to maximize the number of valid subarrays.'''

'''VERY IMPORTANT — When to use CASE 3

Use this pattern when:

Maximum number of subarrays

Non-overlapping windows

Greedy selection

“Pick as early as possible”'''