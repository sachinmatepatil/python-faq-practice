# Using slicing
s = 'Sachin'
rev = s[::-1]  # Fastest and most Pythonic way. Uses slicing with a step of -1
#Now, s[::-1] means: 👉 “Start from the end, take one step backward each time, and collect all letters.”
print(rev)


# Using reversed() with join
s1 = 'sachin'
revstr = ''.join(reversed(s1))  # Built-in function that returns an iterator, good for readability.
print(revstr)

# Using loop
s2 = 'sachin'
rev = ''
for i in s2:
    rev = i + rev
print(rev)


# using recursion
def reversee(s):
    if len(s) == 0:
        return s
    return reversee(s[1:]) + s[0]


print(reversee('sachin'))

# Using stack(list) - Demonstrates knowledge of data structures (LIFO behavior).
s = 'Sachin'
stack = list(s)
revd = ""
while stack:
    revd += stack.pop()
print(revd)

# Using list comprehension - Manual control of indices, good to show comprehension skills.
s = 'SAchind'
rev = ''.join([s[i] for i in range(len(s) - 1, -1, -1)])
print(rev)
# 1️⃣ len(s) → gives total letters in "stringkkkll" → 11
# 2️⃣ range(len(s)-1, -1, -1) → means
# “Start from index 10 (last letter), go till index -1, and move one step backward each time.”
# 👉 So it counts 10, 9, 8, ..., 0
# 3️⃣ [s[i] for i in ...] → collects letters from end to start.
# → makes a list like ['l', 'l', 'k', 'k', 'k', 'g', 'n', 'i', 'r', 't', 's']
# 4️⃣ ''.join(...) → joins all those letters together into a string.

# Using reduce() from functools - Functional programming approach — rarely used but shows depth.
from functools import reduce

s = 'Samsasd'
rev = reduce(lambda x, y: y + x, s)
print(rev)

# | # | Method                          | Code Sketch                                            | Time      | Extra Space                           | Notes / Gotchas                                                               |
# | - | ------------------------------- | ------------------------------------------------------ | --------- | ------------------------------------- | ----------------------------------------------------------------------------- |
# | 1 | **Slicing**                     | `s[::-1]`                                              | **O(n)**  | **O(n)**                              | Fastest & most Pythonic. Allocates a new string.                              |
# | 2 | **`reversed()` + `''.join()`**  | `''.join(reversed(s))`                                 | **O(n)**  | **O(n)**                              | Clean, uses an iterator; same asymptotics as slicing.                         |
# | 3 | **Loop w/ string concat**       | `for c in s: rev = c + rev`                            | **O(n²)** | **O(n)**                              | Repeated string concatenation is quadratic → **avoid** for large n.           |
# | 4 | **Recursion**                   | `reverse(s[1:]) + s[0]`                                | **O(n²)** | **O(n)** result + **O(n)** call stack | Demonstrates recursion, but inefficient and hits recursion depth for large n. |
# | 5 | **Explicit stack (list + pop)** | `stack=list(s); rev=''; while stack: rev+=stack.pop()` | **O(n²)** | **O(n)**                              | Pop is O(1) but string concat in loop makes it **O(n²)**.                     |
# | 6 | **List comprehension + join**   | `''.join([s[i] for i in range(len(s)-1,-1,-1)])`       | **O(n)**  | **O(n)**                              | Efficient; comprehension builds list once, then join.                         |
# | 7 | **`functools.reduce`**          | `reduce(lambda x,y: y+x, s)`                           | **O(n²)** | **O(n)**                              | Functional but quadratic due to concat; **avoid** for performance.            |


# Quick takeaways (what interviewers love)
#
# Best practical answers: s[::-1] or ''.join(reversed(s)) (both O(n) time, O(n) space).
#
# Show depth: Mention why naive concatenation is O(n²) (strings are immutable; each concat copies).
#
# Recursion caveat: Adds call-stack overhead and can hit recursion limits on long strings.
#
# If asked to “optimize the loop”:
#
# # O(n) time using list buffer + join
# buf = []
# for i in range(len(s)-1, -1, -1):
#     buf.append(s[i])
# rev = ''.join(buf)