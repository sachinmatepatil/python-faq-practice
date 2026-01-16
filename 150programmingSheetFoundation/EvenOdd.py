'''Problem Statement
One day, while teaching your little sibling about numbers, you wonder how a computer can tell if a number is even or odd. You recall that even numbers are divisible by 2 without a remainder, and odd numbers are not. To make it clear, you decide to write a simple program that checks the divisibility by 2 to classify any given number.

Examples
Input:
number = 4
Output:
Even
Explanation:
4 divides evenly by 2, so it is Even.
Input:
number = 13
Output:
Odd
Explanation:
13 does not divide evenly by 2, so it is Odd.
Input:
number = 0
Output:
Even
Explanation:
0 divides evenly by 2, so it is Even.'''

user_input = int(input("Enter number"))

def odd_even(user_input):
    if (user_input % 2) == 0 : # Check if the number is divisible by 2
        return "Even"
    else:
        return "Odd"

print(odd_even(user_input))