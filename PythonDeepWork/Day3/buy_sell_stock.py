def max_profit(prices):

    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            max_profit = max(max_profit, profit)
    return max_profit

prices = [7, 1, 5, 3, 6, 4]

print(max_profit(prices))


"""Problem

Prices list:

[7, 1, 5, 3, 6, 4]


You want:

Buy at one day

Sell later

Maximize profit

Example:
Buy at 1
Sell at 6
Profit = 5

Return:

5


If price only goes down, profit = 0.

🧒 Beginner Explanation

Walk through prices like reading a book.

Keep track of:

min_price → lowest price seen so far

max_profit → best profit so far

For each price:

Check if it’s smaller than min_price → update

Else calculate profit with (price - min_price)

See if this is best profit

🟦 Dry Run Example
prices = [7, 1, 5, 3, 6, 4]
min_price = infinity
max_profit = 0


Go through list:

Price	min_price	profit	max_profit
7	7	0	0
1	1	0	0
5	1	4	4
3	1	2	4
6	1	5	5
4	1	3	5

Final answer: 5
Time Complexity → O(n)
Space Complexity → O(1)
"""

