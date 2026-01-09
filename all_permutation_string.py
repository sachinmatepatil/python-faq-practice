string = 'sachin'

def all_permutation_string(string):
    if len(string) == 0:
        return ['']

    permutations = []
    for i, char in enumerate(string):
        # Get the remaining characters after removing the current character
        remaining = string[:i] + string[i+1:]
        # Generate all permutations of the remaining characters
        for perm in all_permutation_string(remaining):
            permutations.append(char + perm)

    return permutations

print(all_permutation_string(string))