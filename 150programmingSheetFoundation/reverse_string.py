'''Problem Statement
While working on a text-based game, you need to reverse strings entered by players for a secret code. You decide to create a simple function that reverses any input string so that the game can process these secret messages.

Examples
Input:
string = "hello"
Output:
"olleh"
Explanation:
Reversing "hello" results in "olleh".
Input:
string = "racecar"
Output:
"racecar"
Explanation:
"racecar" is a palindrome; reversing it results in the same string.
Input:
string = "12345"
Output:
"54321"
Explanation:
Reversing "12345" results in "54321"'''

def rev_str(string):
    new_str = ''

    for ch in string:
        new_str = ch + new_str
    return new_str


string = 'hello'
print(rev_str(string))
# Time complexity - O(n2)
# space complexity - O(n)

s = 'hello'
def rev_str(s):
    rev = list(s)
    rev_str = ''.join(reversed(rev))
    return rev_str
print(rev_str(s))
# Time O(n)
# space O(n)

s = 'hello'
def rev_str(s):
    rev = list(s)
    rev.reverse()
    return ''.join(rev)
print(rev_str(s))
# Time O(n)
# space O(n)