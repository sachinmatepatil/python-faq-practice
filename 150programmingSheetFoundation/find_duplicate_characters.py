# Find Duplicates: Find duplicate characters in an array or string.

def char_frequency(input_string):
    freq = {}

    for ch in input_string:
        freq[ch] = freq.get(ch, 0 ) + 1

    result = []
    for ch,count in freq.items():
        if count > 1:
            result.append(ch)

    return result
input_string = "programming"
print(char_frequency(input_string))