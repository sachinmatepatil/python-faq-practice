'''
The factorial of a number can be very large, but what if you want to know the sum of all its digits? Like breaking down a giant treasure chest into smaller gems, you must calculate the sum of the digits of the factorial.
'''

# def sum_of_factorial_digits(n):
#     # Function to calculate factorial
#     def factorial(num):
#         if num == 0 or num == 1:
#             return 1
#         result = 1
#         for i in range(2, num + 1):
#             result *= i
#         return result
#
#     # Calculate factorial of n
#     fact = factorial(n)
#
#     # Convert factorial to string and sum the digits
#     digit_sum = sum(int(digit) for digit in str(fact))
#
#     return digit_sum
#time complexity O(n) space O(1)


# other way to solve
def sum_fact(n):
    if n == 0 or n == 1:
        return 1
    fact = 1
    for i in range(2, n+1):
        fact *= i
    # Method1
    # total=0
    # str_fact = str(fact)
    # for ch in str_fact:
    #     total +=int(ch)
    # return total

    # using inbuilt sum
    # total = sum(int(ch) for ch in str_fact)
    # return total

    #using simple logic
    total = 0
    while fact>0:
        total += fact%10
        fact//=10
    return total

print(sum_fact(5))
#time complexity by other method is O(n) and space O(1)