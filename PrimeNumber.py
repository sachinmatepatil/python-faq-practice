

# 2 Write a program to check whether number is prime or not
#Logic
# Number > 1 and which has only 2 factors 1 and itself
# Method 1
# def isPrime(n):
#     count=0
#     if n<2:
#         return False
#     for i in range(1,n+1):
#         if (n%i)==0:
#            count=count+1
#     if count == 2:
#         return True
#     else:
#         return False
# x=isPrime(19)
# print(x)
#Method 2 : optimized
# def is_prime(num):
#     # Numbers less than 2 are not prime
#     if num < 2:
#         return False
#
#     # Check for factors from 2 to the square root of the number
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:  # If divisible, it's not prime
#             return False
#
#     return True  # If no factors were found, it's prime
#
#
# # Test the function
# number = int(input("Enter a number to check if it's prime: "))
# if is_prime(number):
#     print(f"{number} is a prime number.")
# else:
#     print(f"{number} is not a prime number.")
# Explanation:
# Numbers Less Than 2:
#
# Numbers like 0 and 1 are not prime, so we immediately return False if num < 2.
#
# Efficient Check:
#
# Instead of checking all numbers from 2 to num-1, we check only up to sqrt(num). If num has any divisors other than 1 and itself, one of them must be ≤ sqrt(num).
#
# Divisibility Check:
#
# If num % i == 0, the number is divisible by i and is therefore not prime.
#
# Return True:
#
# If no divisors are found, the number is prime.
