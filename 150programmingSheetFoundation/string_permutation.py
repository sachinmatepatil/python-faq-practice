'''
• String Permutations: Write a program to print all permutations of a given string (e.g., input "ab" -> "ab", "ba").
'''

def permutation(s):
    result = []

    def backtrack(remaining, path):
        if len(remaining) == 0:
            result.append(path)
            return

        for i in range(len(remaining)):
            ch = remaining[i] #choose character at index i
            new_remaining = remaining[:i] + remaining[i+1:] #remaining string without choosen character
            backtrack(new_remaining, path + ch) #recursice call
    backtrack(s, "")
    return result

s='abcd'
print(permutation(s))


