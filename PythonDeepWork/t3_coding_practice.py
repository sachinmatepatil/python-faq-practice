s = 'sachin'
# x = s[::-1]
# print(x)
#
# y = ''.join(reversed(s))
# print(y)
#
# rev = ''
# for i in s:
#     rev = i + rev
# print(rev)
#
#
# def reversee(s):
#     if len(s) == 0:
#         return s
#     return reversee(s[1:]) + s[0]
#
#
# stack = list(s)
# revd = ""
# while stack:
#     revd += stack.pop()
#     print(revd)

# rev = ''.join(s[i] for i in range(len(s) - 1, -1, -1))
# print(rev)

# from functools import reduce
#
# rev = reduce(lambda x, y: y + x, s)
# print(rev)


#To check valid Anagram

def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    count = {}
    for char in s1:
        count[char] = count.get(char, 0) + 1
    for char in s2:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1
    return True

s1 = "listen"
s2 = "silent"
print(is_anagram(s1, s2))  # Output: True