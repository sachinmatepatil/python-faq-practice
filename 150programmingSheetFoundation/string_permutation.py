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

s='ab'
print(permutation(s))

#Time complexity: O(n * n) #As we explore all possibilities
#Space complexity: O(n!) #as storing all permutations

#Method 2 : without using recursion and backtracking

def permutation_2(s):
    perms = [""]

    for ch in s:
        new_perms = []
        for p in perms:
            for i in range(len(p) + 1):
                new_perms.append(p[:i] + ch + p[i:])
        perms = new_perms
    return perms
print(permutation_2(s))

