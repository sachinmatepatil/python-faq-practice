'''QUESTION 1 — First Unique Character

👉 Problem:
Given a string, return the first character that appears only once.
If none exist, return -1.

Examples:

Input: "sachin"
Output: "s"

Input: "aabbccdee"
Output: "d"

Input: "aabb"
Output: -1
'''

def first_unique_character(st):
    char_count = {} #to storer character count

    for char in st: # iterate through each character in string to count first unuique character
        if char not in char_count:
            char_count[char]=1
        else:
            char_count[char]+=1

        #char_count[char]= char_count.get(ch,0)+1 # above if else can be written like this as well

    for char in st: # to find the first unique
        if char_count[char]==1:
            return char
    return -1


# Test cases
print(first_unique_character("sachin"))      # Output: "s"
print(first_unique_character("a"))
print(first_unique_character("aabbccdee"))


'''“I create a dictionary to count occurrences of each character.
Then I iterate the string again to find the first character with frequency 1.
This solution is O(n) time and O(1) extra space because the character set is fixed.”'''