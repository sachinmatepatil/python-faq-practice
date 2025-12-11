logs = [
    {"user": "A", "day": 1},
    {"user": "A", "day": 2},
    {"user": "A", "day": 4},
    {"user": "B", "day": 1},
    {"user": "B", "day": 3},
    {"user": "B", "day": 4},
]


def longest_consecutive_login_streak(logs):
    window = {}
    result = {}

    #group days by user
    for log in logs:
        user = log['user']
        day = log['day']

        if user not in window:
            window[user] = []
        window[user].append(day)


        for user,days in window.items():
            days.sort()


        # Calculate longest consecutive streak
        max_steak = 1
        current_streak = 1
        for i in range(1, len(days)):
            if days[i] == days[i-1] + 1:
                current_streak +=1
            else:
                max_steak = max(max_steak, current_streak)
                current_streak=1

        max_steak = max(max_steak, current_streak)
        result[user]= max_steak
    return result


print(longest_consecutive_login_streak(logs))


'''I grouped all login days by user, sorted them, and then scanned for consecutive sequences.
If two days are exactly 1 apart, I extend the streak; otherwise, I reset it.
I track the maximum streak for each user.
This runs in O(n log n) due to sorting per user.”'''