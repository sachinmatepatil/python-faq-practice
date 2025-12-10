logs = [
    {"machine": "M1", "event": "start", "load": 10},
    {"machine": "M2", "event": "start", "load": 20},
    {"machine": "M1", "event": "update", "load": 15},
    {"machine": "M2", "event": "stop"},
    {"machine": "M1", "event": "stop"},
]
'''❗ TASK
Return the final state of each machine.

Rules:

"start" → machine is active with initial load

"update" → update load (only if active)

"stop" → machine becomes inactive

Expected Output:
python
Copy code
{
    "M1": {"active": False, "load": 15},
    "M2": {"active": False, "load": 20}
}
'''

logs = [
    {"machine": "M1", "event": "start", "load": 10},
    {"machine": "M2", "event": "start", "load": 20},
    {"machine": "M1", "event": "update", "load": 15},
    {"machine": "M2", "event": "stop"},
    {"machine": "M1", "event": "stop"},
]


def system_state_update(logs):
    final_state = {}

    for log in logs:
        machine = log['machine']
        event = log['event']


        if machine not in final_state:
            final_state[machine] = {"active":False, "load":0}

        if event == 'start':
            final_state[machine]['active']=True
            final_state[machine]['load']=log['load']

        elif event == 'update':
            if final_state[machine]['active']:
                final_state[machine]['load']=log['load']

        elif event == 'stop':
            final_state[machine]['active']=False

    return final_state


print(system_state_update(logs))


'''⭐ SIMPLE EXPLANATION FOR INTERVIEW

“I maintain a dictionary where each machine has its own state with two fields: active and load.
When I see a start event, I activate the machine and set its load.
When I see an update, I update the load only if it’s currently active.
When I see a stop, I mark the machine inactive but retain its last load.
This processes all logs in O(n) time.”'''