# Character Frequency: Count the number of occurrences of each character in a string

input_string = "hello world"

def char_frequency(input_string):
    freq = {}

    for ch in input_string:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq
print(char_frequency(input_string))
