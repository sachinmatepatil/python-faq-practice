def is_valid_parantheses(s):
    stack = []
    mappings = {")":"(","}":"{","]":"["}

    for ch in s:
        if ch in mappings.values():
            stack.append(ch)
            print(stack)
        else:
            if not stack or stack[-1] != mappings[ch]:
                return False
            stack.pop()

    return len(stack) == 0

# VALID PARENTHESES (Beginner Breakdown)
#
# ❓ Problem
#
# Given a string with brackets:
#
# "()[]{}"
#
#
# or
#
# "({[]})"
#
#
# Check if the string is valid.
#
# A string is valid if:
#
# Every opening bracket has a matching closing bracket
#
# Close brackets come in correct order
#
# Examples:
#
# "()" → valid
# "([])" → valid
# "(]" → NOT valid
# "([)]" → NOT valid
#
# 🧒 Beginner-Friendly Explanation
#
# Use a stack (a vertical pile).
#
# Whenever you see:
#
# Opening bracket ( or { or [ → push to stack
#
# Closing bracket ) or } or ] → check top of stack
#
# Rules:
#
# Top of stack must contain the matching opening bracket
#
# If mismatch → invalid
#
# If stack empty at end → valid
#
# 🟦 Dry Run Example: "([])"
#
# Stack initially:
#
# []
#
#
# Read characters:
#
# ( → push → ["("]
#
# [ → push → ["(", "["]
#
# ] → matches top "[" → pop → ["("]
#
# ) → matches top "(" → pop → []
#
# Stack empty → valid.
#
# 🟦 Interview-Level Code
# def is_valid_parentheses(s):
#     stack = []
#     mapping = {')': '(', '}': '{', ']': '['}
#
#     for ch in s:
#         if ch in mapping.values():  # opening brackets
#             stack.append(ch)
#         else:  # closing brackets
#             if not stack or stack[-1] != mapping[ch]:
#                 return False
#             stack.pop()
#
#     return len(stack) == 0
#
# Time Complexity: O(n)
# Space Complexity: O(n) (worst case stack)