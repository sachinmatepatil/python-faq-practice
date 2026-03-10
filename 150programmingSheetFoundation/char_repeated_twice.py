# Repeated Characters: Write a program to print characters that are repeated exactly twice in a string.

#Method 1
def two_times_repeated_characters(input_string):
    freq = {}

    for ch in input_string:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1

    for ch in freq:
        if freq[ch] == 2:
            return ch

input_string = "programming"
print(two_times_repeated_characters(input_string))

#Method 2
def method2(input_string):
    freq = {}
    for ch in input_string:
        freq[ch] = freq.get(ch, 0) + 1

    for ch,count in freq.items():
        if count == 2:
            return ch

input_string = "programming"
print(method2(input_string))

#time complexity: O(n) where n is the length of the input string. We traverse the string once to build the frequency dictionary and then traverse the dictionary to find characters that are repeated exactly twice.
#space complexity: O(k) where k is the number of unique characters in the input string. In the worst case, if all characters are unique, the space complexity would be O(n).
