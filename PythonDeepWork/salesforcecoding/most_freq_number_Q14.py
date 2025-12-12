
def most_frequent_number(nums):

    dict = {}

    for num in nums:
        print(dict)
        if num not in dict:
            dict[num ] =1
        else:
            dict[num ]+=1
    most_freq_num = max(dict ,key=dict.get)
    return most_freq_num

nums = [2 ,3 ,2 ,5 ,3 ,2 ,4 ,3 ,3 ,2 ,2 ,2]
print(most_frequent_number(nums))

'''To find the most frequent number, I used a dictionary to count occurrences.
I loop over the list, and for each number, if it’s not already in the dictionary, I initialize its count to 1; otherwise, I increment the existing count.
After building this frequency map, I use max(dict, key=dict.get) to return the key with the highest count.
This solution runs in O(n) time because each number is processed once, and dictionary lookups are O(1)'''