# Even Length Words: Print only the words in a string that have an even length.

s = 'Print only the words in a string that have an even length'


def w_even(s):
    new_s = s.split()
    words = []
    for ch in new_s:
        if len(ch) % 2 == 0:
            words.append(ch)

    return words


print(w_even(s))


def w_even(s):
    return [word for word in s.split() if len(word) % 2 == 0]

print(w_even(s))

