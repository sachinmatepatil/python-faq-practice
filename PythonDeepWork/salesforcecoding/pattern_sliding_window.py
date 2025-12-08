'''SLIDING WINDOW — Main Concept

We use this pattern whenever the problem says:

“Longest substring…”

“Maximum window…”

“Count something inside a window that moves…”

“No repeating characters…”

“At most K… / At least K…”

The window grows (right pointer moves right)
and shrinks (left pointer moves right).'''

#Problem - longest substring without repeating characters

'''Example: "abcabcbb" → 3
"bbbb" → 1
"pwwkew" → 3'''

def length_of_longest_substring(s):
    seen = {}
    left = 0
    max_len = 0

    for right in range(len(s)):
        ch = s[right]
        # print(ch)

        if ch in seen and seen[ch]>=left:
            left = seen[ch] + 1
        seen[ch] = right
        max_len = max(max_len, right-left + 1)
        print(max_len)
    return max_len

length_of_longest_substring("abcabcbb")
# length_of_longest_substring("bbbb")