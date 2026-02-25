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