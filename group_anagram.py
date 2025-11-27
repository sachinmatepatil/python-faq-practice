#program for group anagrams

def group_anagram(words):

    groups={}

    for word in words:
        sorted_word = ''.join(sorted(word)) #turn word into sorted string
        if sorted_word not in groups:
            groups[sorted_word]=[]  #Create new group if not exists

        groups[sorted_word].append(word) #Add word to the correct group

    return list(groups.values())


#Expample usage
words = ["eat", "tea", "tan", "ate", "nat", "bat","mate"]
print(group_anagram(words))  #Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]



#
# You will understand:
#
# What an anagram really is
#
# Why we need a “key”
#
# How grouping works
#
# Step-by-step dry run
#
# Dictionary usage
#
# Full beginner explanation
#
# This will become one of your strongest Python skills.
#
# 🟦 WHAT IS AN ANAGRAM (FUN WAY)
#
# Two words are anagrams if:
#
# 👉 They use the exact same letters
# 👉 In any order
#
# Examples:
#
# eat, tea, ate → anagrams
# tan, nat → anagrams
# bat → no match
#
# 🟦 THE PROBLEM
#
# Given:
#
# ["eat","tea","tan","ate","nat","bat"]
#
#
# Group the words that are anagrams:
#
# [
#   ["eat","tea","ate"],
#   ["tan","nat"],
#   ["bat"]
# ]
#
# 🟦 BIGGEST LOGIC OF THIS PROBLEM
#
# If two words are anagrams,
# their sorted version will be the same.
#
# Example:
#
# eat → aet
# tea → aet
# ate → aet
#
#
# So “aet” becomes the key for this group.
#
# 🟦 Beginner Logic
#
# Create an empty dictionary.
#
# For each word:
#
# Sort the letters → this becomes key.
#
# Add the original word inside dictionary under that key.
#
# Finally return all grouped values.
#
# 🟦 VISUAL DRY RUN
# Input:
# ["eat", "tea", "tan", "ate", "nat", "bat"]
#
# Dictionary starts empty:
# {}
#
# 🔹 Word = "eat"
#
# Sort:
#
# eat → aet
#
#
# Dictionary becomes:
#
# {
#   "aet": ["eat"]
# }
#
# 🔹 Word = "tea"
#
# Sort:
#
# tea → aet
#
#
# Dictionary updates:
#
# {
#   "aet": ["eat", "tea"]
# }
#
# 🔹 Word = "tan"
#
# Sort:
#
# tan → ant
#
#
# Dictionary:
#
# {
#   "aet": ["eat", "tea"],
#   "ant": ["tan"]
# }
#
# 🔹 Word = "ate"
#
# Sort:
#
# ate → aet
#
#
# Dictionary:
#
# {
#   "aet": ["eat", "tea", "ate"],
#   "ant": ["tan"]
# }
#
# 🔹 Word = "nat"
#
# Sort:
#
# nat → ant
#
#
# Dictionary:
#
# {
#   "aet": ["eat", "tea", "ate"],
#   "ant": ["tan", "nat"]
# }
#
# 🔹 Word = "bat"
#
# Sort:
#
# bat → abt
#
#
# Dictionary:
#
# {
#   "aet": ["eat", "tea", "ate"],
#   "ant": ["tan", "nat"],
#   "abt": ["bat"]
# }
#
# 🟦 FINALLY
#
# Return list of grouped values:
#
# [
#   ["eat","tea","ate"],
#   ["tan","nat"],
#   ["bat"]
# ]
#
#
# 🟦 Group Anagrams – Time Complexity
#
# Let:
#
# n = number of words
#
# k = max length of each word
#
# 🟦 Approach Used → Sorting Each Word
# key = "".join(sorted(word))
#
#
# Sorting each word takes:
#
# O(k log k)
#
#
# We do this for every word, so total:
#
# O(n * k log k)
#
#
# This is the standard time complexity accepted in interviews.
#
# 🟦 Explained Like a Kid
#
# You sort each word’s letters.
# Sorting takes time depending on the number of letters (k log k).
#
# You do this for every word (n words) →
# so n times sorting cost →
# → n × (k log k).
#
# 🟦 Dictionary Insertions?
#
# Dictionary insert is O(1) average.
#
# So the main time cost is sorting.
#
# 🟦 FINAL ANSWER (Interview Line)
# Time Complexity: O(n * k log k)
#
# sorting each of n words of length k → O(k log k)
#
# total → O(n k log k)
#
# Space Complexity: O(n * k)
#
# storing all words in grouped lists
#
# dictionary keys also take space