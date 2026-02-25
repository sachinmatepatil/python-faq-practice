'''
• Reverse Only Letters: Reverse a string but keep non-letter characters (numbers, symbols) in their original positions.
'''

def rev_only_letters(s):
    st = list(s) # Convert string to list for mutability
    left , right = 0 , len(st) - 1

    while left < right:
        if not st[left].isalpha():
            left+=1
        elif not st[right].isalpha():
            right-=1
        else:
            st[left], st[right] = st[right], st[left]
            left+=1
            right-=1
    return ''.join(st)

s = "a-bC-dEf-ghIj"
print(rev_only_letters(s))