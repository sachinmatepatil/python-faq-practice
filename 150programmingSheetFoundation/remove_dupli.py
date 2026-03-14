# Remove Duplicates: Remove duplicate characters from a string and print only unique characters.

#MEthod 1
def rem_d(s):
    seen = set()
    result = []

    for ch in s:
        if ch not in seen:
            result.append(ch)
            seen.add(ch)

    return ''.join(result)

s = "programming"
print(rem_d(s))
#time complexity: O(n)
#space complexity: O(n)



#Method 2
def rem_d_2(s):
    return ''.join(dict.fromkeys(s))
print(rem_d_2('programming'))
#time complexity: O(n)
#space complexity: O(n)