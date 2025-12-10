'''⭐ Q2 — GROUPING USING DICTIONARY (Medium Warm-up)

This is CRITICAL because Salesforce code-pair heavily uses:

grouping

counting

dictionary accumulation

restructuring data

🟦 Q2 — Problem: Group Words by Their First Letter
Input:
["apple", "banana", "apricot", "berry", "cherry", "carrot"]

Output:
{
  "a": ["apple", "apricot"],
  "b": ["banana", "berry"],
  "c": ["cherry", "carrot"]
}

Task:

Write Python code to group words by their starting letter.

This is EXTREMELY important, because many Salesforce problems require:

grouping logs by category

grouping events by user

grouping items by type

This is the foundation.'''


words = ["apple", "banana", "apricot", "berry", "cherry", "carrot"]

def group_by_first_letter(words):
    group = {} # Empty dic to store grouped words

    for word in words:
        if word[0] not in group:
            group[word[0]] = [word]
        else:
            group[word[0]]+= [word]
    return group

# Aleternative approach

def group_by_first_letter_alternative(words):
    group = {}

    for word in words:
        group.setdefault(word[0],[]).append(word)
    return group

# Test case
print(group_by_first_letter(words))
print(group_by_first_letter_alternative(words))

'''I iterate through each word and use a dictionary where the key is the first letter.
If the key doesn’t exist, I initialize it with a list; otherwise, I append the word.
This lets me group all words starting with the same letter in O(n) time.'''