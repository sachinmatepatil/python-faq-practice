# Reverse Only Letters: Reverse a string but keep non-letter characters (numbers, symbols) in their original positions.

#MEthod 1 : using empty string and iterating through the string

s = "I love india"
def rev_s(s):
    new_s = s.split()
    rev = ''

    for ch in new_s:
        rev = ch + ' ' + rev
    return rev.strip()

print((rev_s(s)))

#Method 2 : using list slicing

def rev_s2(s):
    return ' '.join(s.split()[::-1])

print(rev_s2(s))