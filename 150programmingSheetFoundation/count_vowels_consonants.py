'''You receive a mysterious message. To decode its tone—whether it's a whisper of vowels or a march of consonants—you must count how many vowels and consonants it contains.
'''


def count_v_c(s):
    vowe = 0
    consonants = 0

    vowels = ['a', 'e', 'i', 'o', 'u']

    for ch in s.lower():
        if ch.isalpha():
            if ch in vowels:
                vowe += 1
        else:
            consonants += 1
    return vowe, consonants


s = 'openai'
print(count_v_c(s))

# ⏱️ Time Complexity
# 	•	Loop runs once per character → n times
# 	•	ch in vowels checks a list of size 5 → constant time
#
# ✅ Time Complexity = O(n)
#
# ⸻
#
# 💾 Space Complexity
# 	•	Uses a fixed list of vowels (size 5)
# 	•	Uses a few counters
#
# ✅ Space Complexity = O(1)

'''🎤 Interview One-Liner

I iterate through the string once, classify each alphabet character as vowel or consonant using a set for constant-time lookup, resulting in O(n) time and O(1) space.
'''