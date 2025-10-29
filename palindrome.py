# To check whether string is palindrome

# s = input('Enter a string')

# Method 1
# value=s[::-1]
# if value==s:
#     print('String is palindrome')
# else:
#     print('Not palindrome')


# Method 2
# s_normal = s.lower().replace(' ', '')

# Initialize two pointers
# left = 0
# right = len(s_normal) - 1

# Compare characters from both ends
# is_pal = True
# while left < right:
#     if s_normal[left] != s_normal[right]:
#         is_pal = False
#     left += 1
#     right -= 1
#
# # Output result
# if is_pal:
#     print('PAliindrome')
# else:
#     print('Not a palindrome')

# 🧠 Explanation:
# Convert the string to lowercase and remove spaces to standardize the comparison.
#
# Use two pointers: one starting from the beginning (left), and one from the end (right).
#
# Compare characters until the pointers meet or cross.


