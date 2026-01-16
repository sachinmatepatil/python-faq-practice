'''Problem Statement
Your math teacher challenges you to find the sum of the first N natural numbers. You recall the formula: sum = N * (N + 1) / 2. Instead of adding them one by one, you decide to write a program that uses this formula to quickly compute the sum for any given N.

Examples
Input:
N = 5
Output:
15
Explanation:
Sum of 1 + 2 + 3 + 4 + 5 = 15.
Input:
N = 10
Output:
55
Explanation:
Sum of first 10 natural numbers = 55.
Input:
N = 1
Output:
1
Explanation:
Sum of first natural number (1) is 1.'''

num = 10
def sum_of_num(num):
    if num < 0:
        return False

    for i in range(num):
        sum = num * (num + 1) // 2
    return sum


print(sum_of_num(num))
