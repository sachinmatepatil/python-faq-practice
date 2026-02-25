'''
• Reverse Only Vowels: Reverse only the vowels in a string, leaving consonants and other characters in place.
'''

def reverse_vowels(s):

    s_list = list(s)
    vowels = set('aeiouAEIOU')
    left, right = 0, len(s) -1

    while left < right:
        if s_list[left] not in vowels:
            left += 1
        elif s_list[right] not in vowels:
            right -= 1
        else:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
    return ''.join(s_list)

#example test cases
print((reverse_vowels('hello')))  # Output: 'holle'
print((reverse_vowels('leetcode')))  # Output: 'leotcede'
