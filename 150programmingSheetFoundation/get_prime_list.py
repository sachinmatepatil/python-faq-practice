'''
Prime numbers are the building blocks of all numbers, indivisible except by 1 and themselves. Your mission is to identify and list all such prime numbers that are smaller than a given number. Can you help reveal this secret list of prime guardians?
'''

import math


def get_prime(n):
    # Initialize an empty list to store the primes we discover
    prime_list = []

    # Outer Loop: Iterate through every number from 2 up to 'n'
    # We start at 2 because 0 and 1 are not prime numbers.
    for num in range(2, n + 1):

        # Assume the number is prime until we prove otherwise
        is_prime = True

        # Inner Loop: Check for factors starting from 2
        # Optimization: We only need to check up to the square root of 'num'
        # int(num**0.5) + 1 ensures the range includes the square root value
        for i in range(2, int(num ** 0.5) + 1):

            # If 'num' is divisible by 'i', it's not prime
            if num % i == 0:
                is_prime = False  # Flip the flag
                break  # Exit the inner loop early (efficiency)

        # If the flag remained True, the number is prime!
        if is_prime:
            prime_list.append(num)

    return prime_list


# Execute the function and print the results
print(get_prime(20))

'''Approach Explanation:'''
'''
The Approach: "Trial Division"The approach used in this code is known as Trial Division. 
It is the most straightforward way to determine if a number is prime.
1. The StrategyThe fundamental definition of a prime number is that it has no divisors other than 1 and itself. Therefore, our strategy is to try and divide each number by everything else. 
If we find even one number that divides it perfectly (remainder of 0), 
we instantly know it isn't prime.
2. The Efficiency Trick (Square Root Limit)The most important part of this approach is the limit of the inner loop: int(num**0.5) + 1.Imagine you are checking if 36 is prime:Factors come in pairs: $(2, 18), (3, 12), (4, 9), (6, 6)$.
Notice that once you pass the square root ($6$), the factors just repeat in reverse order ($9 \times 4$, $12 \times 3$, etc.).By stopping at the square root, you cut the amount of work significantly.
 For a number like 1,000,000, instead of checking 1,000,000 numbers, you only check 1,000.
3. The "Flag" PatternUsing a variable like is_prime = True is a common programming pattern. 
It allows the inner loop to "signal" the outer loop.
 Think of it like a security guard: the guard assumes a person is safe (True) unless they catch them doing something wrong—at which point they label them "not safe" (False) and stop watching them (break).


'''


'''
Time Complexity: O(n\sqrt{n}) — You check $n$ numbers, and for each, you do up to $\sqrt{num}$ checks.
Space Complexity: O(p) — You only use extra space to store the $p$ prime numbers found.
'''
