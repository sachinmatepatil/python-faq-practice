logs = [
    {"event": "login", "user": "A"},
    {"event": "click", "user": "A"},
    {"event": "login", "user": "B"},
    {"event": "logout", "user": "A"},
    {"event": "click", "user": "C"},
]


def group_logs_by_user(logs):
    count_log_user = {}

    for log in logs:
        if log['user'] not in count_log_user:
            count_log_user[log['user']] = [log['event']]
        else:
            count_log_user[log['user']] += [log['event']]
    return count_log_user


print(group_logs_by_user(logs))


def group_logs_by_user_alter(logs):
    count_log_user = {}

    for log in logs:
        user = log['user']
        event = log['event']
        count_log_user.setdefault(user, []).append((event))
    return count_log_user


print(group_logs_by_user_alter(logs))

'''I iterate through each log and group events by the user who performed them.
I use a dictionary where each user maps to a list of event names.
If the user doesn’t exist yet, I initialize the list; otherwise, I append the new event.
This solution runs in O(n) time and uses O(u) space where u is number of users.'''
