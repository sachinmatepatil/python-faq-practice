'''
Given a string:"AAABBCCDAA"
:return compressed_string
"A3B2C2D1A2"
'''
s = "AAABBCCDAA"

def compressed_string(s):
    result = ""
    count = 1

    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count+=1
        else:
            result += s[i-1] + str(count)
            count = 0
    return result

print(compressed_string(s))

'''

You should say it like this:
	•	I iterate through the string and count consecutive characters.
	•	If the current character is same as the previous one, I increment the count.
	•	If it changes, I append the previous character and its count to the result.
	•	Finally, I append the last character group.
	•	Time complexity is O(n) since we traverse the string once.
'''

'''

“We initialize count to 1 because the first character already appears once, which avoids off-by-one errors when counting consecutive characters.”'''