'''Problem Statement
You’ve found a ledger of gold coins collected over time. Calculate the total treasure by summing all the entries in this array.'''

'''Examples
Input:
array = [1, 2, 3, 4, 5]
Output:
15'''

arr = [1, 2, 3, 4, 5]


# Method 1 - using in built function
# def total_array(arr):

#     total = sum(arr)
#     return total
# print(total_array(arr))

# Method 2 - using for loop
def total_arr(arr):
    total = 0

    for num in arr:
        total += num
    return total


print(total_arr(arr))

