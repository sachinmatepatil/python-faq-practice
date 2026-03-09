#Pangram Check: Check if a sentence is a Pangram (contains every letter of the alphabet).

s = "The quick brown fox jumps over the lazy dog"
def is_pangram(s):
    letters = set()

    for ch in s.lower():
        if ch.isalpha():
            letters.add(ch)
    return len(letters) == 26

print(is_pangram(s))  # Output: True

import string
def is_anagramv1(s):
    return set(string.ascii_lowercase).issubset(set(s.lower())) #

print(is_anagramv1(s))
