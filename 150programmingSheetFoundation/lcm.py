'''Problem Statement
You’re given two ancient artifacts, each cursed to repeat at their own intervals. To break the cycle and align them perfectly, you must determine the earliest time both will align. In other words, find the Least Common Multiple (LCM) of two numbers.'''


def lcm(n1, n2):
    n1_list = []
    n2_list = []

    for i in range(1, 10):
        num = n1 * i
        n1_list.append(num)

    for i in range(1, 10):
        num = n2 * i
        n2_list.append(num)

    for num in n1_list:
        if num in n2_list:
            return num


print(lcm(10, 20))

#Method 2
# LCM(n1, n2) * GCD(n1, n2) = a * b
def gcd(n1, n2):
    while n2 != 0:
        n1, n2 = n2, n1 % n2
    return n1


def lcm(n1, n2):
    return (n1 * n2) // gcd(n1, n2)


print(lcm(12, 15))

#GCD-based
# time : O(log n)
# space : O(1)

'''
⸻

1) What gcd(n1, n2) means

GCD = Greatest Common Divisor
The largest number that divides both n1 and n2 exactly.

Example:
	•	divisors of 12: 1,2,3,4,6,12
	•	divisors of 15: 1,3,5,15
✅ GCD = 3

⸻

2) GCD Code Explanation (Euclidean Algorithm)

Code:
def gcd(n1, n2):
    while n2 != 0:
        n1, n2 = n2, n1 % n2
    return n1
    
    What’s happening in each line
	•	while n2 != 0:
Keep going until remainder becomes 0.
When remainder is 0, the current n1 is the GCD.
	•	n1 % n2
This gives the remainder when n1 is divided by n2.
	•	n1, n2 = n2, n1 % n2
This is simultaneous assignment:
	•	New n1 becomes old n2
	•	New n2 becomes remainder

Why this works (core idea)

If:
	•	n1 = n2 * q + r  (division algorithm)

Then:
	•	Any number that divides both n1 and n2 also divides r
	•	So:
gcd(n1, n2) = gcd(n2, r)

That’s why we repeatedly replace the pair with (n2, n1 % n2).

⸻

3) Dry Run of gcd(12, 15) (Important)

Start:
	•	n1 = 12, n2 = 15

Iteration 1
	•	n1 % n2 = 12 % 15 = 12
	•	Update:
	•	n1 = 15
	•	n2 = 12

Iteration 2
	•	15 % 12 = 3
	•	Update:
	•	n1 = 12
	•	n2 = 3

Iteration 3
	•	12 % 3 = 0
	•	Update:
	•	n1 = 3
	•	n2 = 0

Loop stops because n2 == 0
✅ Return n1 = 3
So, gcd(12,15) = 3

⸻

4) LCM Explanation

Code:
def lcm(n1, n2):
    return (n1 * n2) // gcd(n1, n2)

Meaning:

LCM = Least Common Multiple
Smallest number that both n1 and n2 divide exactly.

Key relation:
LCM(a,b) \times GCD(a,b) = a \times b

So:
LCM(a,b) = \frac{a \times b}{GCD(a,b)}

We use // (integer division) because result is always a whole number.

⸻

5) Dry Run of lcm(12, 15)
	•	gcd(12,15) = 3
	•	(12 * 15) // 3
	•	180 // 3 = 60

6) Complexity

GCD (Euclidean algorithm)
	•	Time: O(log(min(n1, n2)))
Each step reduces the numbers quickly.
	•	Space: O(1)
Only constant variables.

LCM
	•	Just one multiplication + division + gcd call
So overall same complexity.

⸻

7) Interview-ready one-liner

I compute GCD using the Euclidean algorithm and then use LCM(a,b) = (a*b)/GCD(a,b), which runs in logarithmic time and constant space
'''