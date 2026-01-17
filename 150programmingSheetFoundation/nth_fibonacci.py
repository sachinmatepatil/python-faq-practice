'''Problem Statement
While exploring patterns in nature, you get curious about the Fibonacci sequence — a series where each number is the sum of the two preceding ones. To help generate the sequence quickly, you decide to write a program that calculates the Nth Fibonacci number.

Examples
Input:
N = 6
Output:
8
Explanation:
Fibonacci sequence up to 6 terms: 0, 1, 1, 2, 3, 5, 8.
Input:
N = 1
Output:
0
Explanation:
The first Fibonacci number is 0.
Input:
N = 2
Output:
1
Explanation:
The second Fibonacci number is 1.'''

def fib(n):
    n1 = 0
    n2 = 1

    for i in range(2, n + 1):
        temp = n2 + n1
        n1 = n2
        n2 = temp
    #   print(temp)
    return temp
print(fib(6))

'''⏱️ Time Complexity
	•	The loop runs from 2 to n
	•	One constant-time operation per iteration

✅ Time Complexity = O(n)

⸻

💾 Space Complexity
	•	Only a fixed number of variables (n1, n2, temp)
	•	No extra arrays or recursion stack

✅ Space Complexity = O(1)'''