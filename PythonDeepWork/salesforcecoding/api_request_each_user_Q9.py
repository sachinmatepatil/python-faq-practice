#Program to return how many API calls each user made in the first 5-sec window
logs = [
    {"user": "A", "time": 1},
    {"user": "A", "time": 2},
    {"user": "A", "time": 5},
    {"user": "B", "time": 3},
    {"user": "A", "time": 6},
    {"user": "B", "time": 7},
]

def sliding_window_counts(logs):
    windows = {}   # stores timestamps per user
    result = {}    # stores counts per user

    for log in logs:
        user = log['user']
        time = log['time']

        if user not in windows:
            windows[user] = []
            result[user] = []

        # Add the new timestamp
        windows[user].append(time)

        # Remove timestamps outside 5-sec window
        while windows[user] and time - windows[user][0] >= 5:
            windows[user].pop(0)

        # Number of calls in window = length of window list
        result[user].append(len(windows[user]))

    return result


print(sliding_window_counts(logs))