logs = [
    {"user": "A", "event": "login"},
    {"user": "A", "event": "login"},
    {"user": "A", "event": "logout"},
    {"user": "B", "event": "login"},
    {"user": "A", "event": "logout"},
    {"user": "B", "event": "logout"},
]


def active_session_per_user(logs):
    last_active_session = {}
    # count_active_session = {}

    for log in logs:
        user = log['user']
        event = log['event']
        if user not in last_active_session:
            last_active_session[user] = 0
        if event == 'login':
            last_active_session[user] += 1
        elif event == 'logout':
            last_active_session[user] -= 1
    return last_active_session


print(active_session_per_user(logs))


'''I maintain a dictionary that tracks each user’s current count of active sessions.
When I see a login, I increment the count; when I see a logout, I decrement it.
I initialize each user with zero active sessions the first time they appear.
This solution is O(n) since each log entry is processed once.'''