# Special Character Frequency: Count the frequency of special characters in a string.

def freq_special_char(s):
    freq = {}

    for ch in s:
        if not ch.isalnum() and ch != " ":
            freq[ch] = freq.get(ch, 0) + 1
    return freq

s = "Hello, World! @2024@ #Python"
print(freq_special_char(s))

# Time complexity : O(n) where n is the length of the input string s. We traverse the string once to count the frequency of special characters.
# Space complexity : O(k) where k is the number of unique special characters in the string. In the worst case, if all characters are special and unique, space complexity can be O(n).