'''
Problem Statement
Some numbers are special—they are equal to the sum of their own digits each raised to the power of the number of digits. These are called narcissistic numbers. Your mission is to determine if a given number is one such narcissistic number.
'''
#Method 1: using string conversion
# def to_check_armstron_number(n):
#     numb_str = str(n) # Get the number of digits in the number
#     power = int(len(numb_str)) # Calculate the sum of each digit raised to the power of number of digits
#     total = 0
#     for ch in numb_str:
#         total += int(ch) ** power # Raise each digit to the power and add to total
#
#     if total == n:
#         return True # Check if the total is equal to the original number
#     else:
#         return False
# print(to_check_armstron_number(153))  # True
#time - O(d)
#Space - O(d)

#Method 2: using mathematical operations
def to_check_armstron_number_math(n):
    temp = n #to store copy of original number

    #Step 1: calculate number of digits mathematically
    # use simple logic to get the power
    power = 0
    num_for_count = n
    if num_for_count == 0: power=1 # Edge case for 0
    while num_for_count > 0:
        num_for_count //=10
        power += 1

    #Step 2: calculate sum of each digit raised to the power
    total = 0
    sum_of_powers = n
    while sum_of_powers>0:
        digit = sum_of_powers%10
        total += digit ** power
        sum_of_powers//=10

    if total == n:
        return True
    else:
        return False

print(to_check_armstron_number_math(9474))
#Time - O(d)
#space - O(1)