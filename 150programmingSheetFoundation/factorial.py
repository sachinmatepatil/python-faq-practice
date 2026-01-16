'''Problem Statement
While solving combinatorics problems, you need to calculate factorials of numbers. Factorial of a number N is the product of all positive integers less than or equal to N. To automate this, you decide to write a program that calculates factorials either iteratively or recursively.

Examples
Input:
N = 5
Output:
120
Explanation:
5! = 5 × 4 × 3 × 2 × 1 = 120.
Input:
N = 0
Output:
1
Explanation:
By definition, 0! = 1.
Input:
N = 3
Output:
6
Explanation:
3! = 3 × 2 × 1 = 6.
Close
View Full Detail'''
n = 5
def fact(n):
    if n == 0 or n == 1:
        return 1
    total = 1
    for i in range(1, n + 1):
        total = total * i
        print(i)
        print(total)
    return total


print(fact(n))

#---------------------------
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n * factorial(n-1)
# fa=factorial(5)
# print(fa)

# def factorial(n):
#     return 1 if(n==0 or n==1) else n*factorial(n-1)
# x=factorial(5)
# print(x)