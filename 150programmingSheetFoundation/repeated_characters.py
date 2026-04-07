# Repeated Characters: Write a program to print characters that are repeated exactly twice in a string.


s = 'programming'
def repeated_characters(s):
    seen = {}
    rep = []

    for ch in s:
        seen[ch] = seen.get(ch, 0) + 1

    for ch in seen:
        if seen[ch] == 2:
            rep.append(ch)

    return rep
print(repeated_characters(s))
