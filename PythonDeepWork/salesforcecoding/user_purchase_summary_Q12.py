'''Problem: User Purchase Summary

You’re given a list of purchase logs:

logs = [
    {"user": "A", "amount": 50},
    {"user": "B", "amount": 20},
    {"user": "A", "amount": 30},
    {"user": "C", "amount": 100},
    {"user": "B", "amount": 80},
]

❗ Task 1

For each user, calculate the total purchase amount.

Expected output:

{
    "A": 80,   # 50 + 30
    "B": 100,  # 20 + 80
    "C": 100   # 100
}

❗ Task 2

Also return which user spent the most.

So final result can be like:

{
    "totals": {"A": 80, "B": 100, "C": 100},
    "top_spender": "B"   # or "C" if tie-handling is different
}


(If there is a tie, it’s okay to return any one of the top spenders.)

🧠 Hints (use only if stuck)

Use a dictionary totals to store sum per user.

Pattern is similar to counting, but instead of +1, you do + amount.

To find the top spender: loop over totals and track:

max amount

user with max amount'''

logs = [
    {"user": "A", "amount": 50},
    {"user": "B", "amount": 20},
    {"user": "A", "amount": 30},
    {"user": "C", "amount": 100},
    {"user": "B", "amount": 80},
]

def total_purchase_amount(logs):
    total_purchase = {}

    for log in logs:
        user = log['user']
        amount = log['amount']

        if user not in total_purchase:
            total_purchase[user] = amount
        else:
            total_purchase[user] += amount

    top_spender = max(total_purchase, key=total_purchase.get)

    return {
        "totals": total_purchase,
        "top_spender": top_spender
    }


print(total_purchase_amount(logs))

'''I used a dictionary to sum all purchase amounts per user.
After building the totals, I used max(dict, key=dict.get) to find the user with the highest spending.
The solution is O(n) since each log is processed once.'''