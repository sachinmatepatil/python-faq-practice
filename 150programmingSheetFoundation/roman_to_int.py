# Roman to Integer: Convert a Roman numeral string to an integer.

s = "MCMXCIV"
def roman_to_int(s):
    roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

    total = 0
    prev = 0

    for ch in s:
        if roman[ch] < prev:
            total -= roman[ch]
        else:
            total += roman[ch]
        prev = roman[ch]
    return total

print(roman_to_int(s))

#time complexity: O(n) where n is the length of the input string s, as we need to iterate through each character in the string once.
#space complexity: O(1) because the space used by the dictionary is constant and does