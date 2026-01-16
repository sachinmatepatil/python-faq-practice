'''Problem Statement
In a programming contest, you get a question: determine whether a given number is prime. You remember a prime number is a number greater than 1 that has no divisors other than 1 and itself. To solve this, you decide to check divisibility from 2 up to the square root of the number. This way, you can quickly find if any divisor exists and decide primality.

Examples
Input:
number = 7
Output:
Prime
Explanation:
7 has no divisors other than 1 and 7, so it is Prime.
Input:
number = 4
Output:
Not Prime
Explanation:
4 is divisible by 2, so it is Not Prime.
Input:
number = 2
Output:
Prime
Explanation:
2 is the smallest prime number.'''

#MEthod 1


# user_input = int(input("Enter number"))
#
#
# def prime_number(user_input):
#     if user_input < 2:
#         return False
#
#     count = 0
#
#     for i in range(1, user_input + 1):
#         if (user_input % i) == 0:
#             count += 1
#     if count == 2:
#         return True
#     else:
#         return False
#
#
# print(prime_number(user_input))

# Method 2 : optimized

user_input = int(input("Enter number"))


def prime_number(user_input):
    if user_input < 2:
        return False

    for num in range(2, int(user_input ** 0.5) + 1):
        if (user_input % num) == 0: # If divisible, it's not prime
            return False
    return True # If no factors were found, it's prime


print(prime_number(user_input))