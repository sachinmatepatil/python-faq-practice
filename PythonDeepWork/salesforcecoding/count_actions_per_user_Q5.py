logs = [
    {"event": "login", "user": "A"},
    {"event": "click", "user": "A"},
    {"event": "login", "user": "B"},
    {"event": "logout", "user": "A"},
    {"event": "click", "user": "C"},
]


def count_actions_per_user(logs):
    user_actions = {}

    for log in logs:
        # ensure user dictionary exists
        if log['user'] not in user_actions:
            user_actions[log['user']] = {}

        # count event
        if log['event'] not in user_actions[log['user']]:
            user_actions[log['user']][log['event']] = 1
        else:
            user_actions[log['user']][log['event']] += 1

    return user_actions



print(count_actions_per_user(logs))


def count_actions_per_user_alternative(logs):
    user_actions = {}

    for log in logs:
        user = log['user']
        event = log['event']

        if user not in user_actions:
            user_actions[user] = {}

        if event not in user_actions[user]:
            user_actions[user][event]= 1
        else:
            user_actions[user][event]+=1

        # user_actions[user][event]=user_actions[user].get(event,0)+1
    return user_actions

print(count_actions_per_user_alternative(logs))

'''SIMPLE EXPLANATION FOR THE FULL SOLUTION

“I’m building a nested dictionary where each user maps to another dictionary that counts how many times each event occurs.

As I loop through the logs, I first check if the user exists in the outer dictionary. If not, I initialize it so I can safely store event counts inside it.

Then for each event, I either start the count at 1 or increment it if it has appeared before.

In the end, every user has a dictionary showing how many times they performed each event.

This solution is O(n) because I scan the logs once.”

🟦 ⭐ EVEN SIMPLER VERSION (If your brain freezes in interview)

“For each log, I make sure the user exists in the dictionary.
Then I count how many times each event appears for that user.
I use a nested dictionary: outer keys are users, inner keys are events with their counts.
Everything runs in O(n).”'''