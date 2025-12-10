logs = [
    {"event": "login", "user": "A"},
    {"event": "click", "user": "A"},
    {"event": "login", "user": "B"},
    {"event": "logout", "user": "A"},
    {"event": "click", "user": "C"},
]


def count_logs(logs):
    count_event = {} # to store count of each event

    for log in logs:
        if log['event'] not in count_event:
            count_event[log['event']]=1
        else:
            count_event[log['event']] += 1
    return count_event


print(count_logs(logs))

#Alterntive approach

def count_events_alternative(logs):
    count_logs = {}

    for log in logs:
        event = log['event']
        count_logs[event] = count_logs.get(event, 0) + 1
    return count_logs

print(count_events_alternative(logs))


'''I iterate through each log entry and extract the event field.
Then I maintain a dictionary where the key is the event name and the value is the count.
Each time I see the event, I increment the count.
This runs in O(n) time and uses O(k) space where k is the number of event types.'''