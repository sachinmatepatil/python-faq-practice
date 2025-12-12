def remove_duplicates(s):
    new_string = ''

    for ch in s:
        if ch not in new_string:
            new_string += ch
    return new_string


s = 'programming'
print(remove_duplicates(s))

'''“I created a new string and iterated over each character.
If a character was not already added, I appended it.
This way only the first occurrence is kept.'''

def remove_duplicates(s):
    seen = set()
    result = []

    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result.append(ch)
    return ''.join(result)

print(remove_duplicates(s))

'''Why better?

Set lookup = O(1)

Append list = O(1)

Join at end = O(n)

➡️ Total = O(n)
➡️ Cleaner & faster

🟦 Interview-ready explanation (Optimized version)

“I used a set to track seen characters because lookup is O(1).
For each character, if it’s not in the set, I add it to the result list.
This keeps only first occurrences and runs in linear time.”'''




