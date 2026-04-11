'''
• Replace Vowels: Replace all vowels in a string with the character 'X'.
'''

def replace_vowels(s):
    new_s = list(s)
    vowels = set('aeiouAEIOU')

    for i in range(len(new_s)):
        if new_s[i] in vowels:
            new_s[i] = 'X'
    return ''.join(new_s)

# Example usage:
s = "Hello World!"
result = replace_vowels(s)
print(result)

#time complexity: O(n) where n is the length of the input string s, as we need to iterate through each character in the string once.

#space complexity: O(n) in the worst case, if all characters in the input string are vowels, we would create a new list of the same length as the input string to store the modified characters.