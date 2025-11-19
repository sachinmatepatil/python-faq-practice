def is_anagram(s1, s2):
    if len(s1) !=  len(s2):
        return False
    count = {}
    for char in s1:
        count[char] = count.get(char, 0) + 1
    for char in s2:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False
    return True

s1 = "listen"
s2 = "silent"
print(is_anagram(s1, s2))  # Output: True

#
# 🟦 1️⃣ First check: Are lengths equal?
# if len(s1) != len(s2):
#     return False
#
#
# If one word is longer, they can NEVER be anagrams.
#
# Example:
#
# "cat"  and  "taco"  → different lengths → not anagrams
#
#
# So this is a quick escape.
#
# 🟦 2️⃣ Make an empty dictionary to count letters
# freq = {}
#
#
# Think of it as a letter counter box:
#
# freq = { }
#
#
# We will fill it like:
#
# {'l':1, 'i':1, 's':1, 't':1, 'e':1, 'n':1}
#
# 🟦 3️⃣ Count letters from the first word
# for ch in s1:
#     freq[ch] = freq.get(ch, 0) + 1
#
#
# This means:
#
# 👉 For every letter in s1:
#
# Look inside the dictionary
#
# If the letter is not there → treat count as 0
#
# Add 1
#
# Example with "listen"
#
# Step by step:
#
# ch	freq after adding
# l	{'l': 1}
# i	{'l': 1, 'i': 1}
# s	{'l':1,'i':1,'s':1}
# t	{'l':1,'i':1,'s':1,'t':1}
# e	{'l':1,'i':1,'s':1,'t':1,'e':1}
# n	{'l':1,'i':1,'s':1,'t':1,'e':1,'n':1}
#
# 👉 Now dictionary holds how many times each letter appears.
#
# 🟦 4️⃣ Now subtract counts using the second word
# for ch in s2:
#
#
# For each letter in the second word:
#
# (A) If the letter is NOT in the dictionary → NOT an anagram
# if ch not in freq:
#     return False
#
#
# Example:
#
# s1 = "abc"
# s2 = "abd"  → d is not in freq → return False
#
# (B) Reduce count by 1
# freq[ch] -= 1
#
#
# Because we "used up" one letter.
#
# (C) If count becomes negative → NOT an anagram
# if freq[ch] < 0:
#     return False
#
#
# Example:
#
# s1 = "aabc"
# s2 = "abca" → still ok
# s2 = "abbc" → using 'b' twice → count becomes -1 → not anagram
#
# 🟦 5️⃣ If all letters match perfectly → return True
# return True
#
#
# Meaning every letter in s1 was matched with an equal letter in s2.
#
# 🔥 WHY THIS CODE IS CORRECT
# 
# It checks same length
#
# It checks same letters
#
# It checks same frequency of each letter
#
# It stops early when mismatch happens
#
# Time complexity: O(n) (best approach)