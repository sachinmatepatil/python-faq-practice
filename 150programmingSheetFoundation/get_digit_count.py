'''
Numbers can be long or short, but what if you need to find out exactly how many digits make up a number? Like counting the soldiers in an army, your task is to count how many digits a number contains.
Examples
Input:
number = 12345
Output:
5
'''

n = 238329320


# Method 1
# def get_digit_count(n):
#     count = len(str(n))
#     return count
# print(get_digit_count(n))
#Time - O(d) where d is the number of digits in n
#Space -O(d) as we are using space to store string of digits

# Method 2
# def get_digit_count(n):
#     digit_str = str(n)

#     count = 0
#     for ch in digit_str:
#         count+=1
#     return count
# print(get_digit_count(n))
#Time - O(d) where d is the number of digits in n
#Space -O(d) as we are using space to store string of digits


# Method 3
def get_digit_count_math(n):
    if n == 0: return 1
    n = abs(n)  # Handle negative numbers
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count
print(get_digit_count_math(n))
#Time - O(d) where d is the number of digits in n
#Space -O(1) as we are using constant space
