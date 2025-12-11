#for eah api compute sucess rate %


logs = [
    {"api": "login", "status": 200},
    {"api": "login", "status": 500},
    {"api": "login", "status": 200},
    {"api": "payment", "status": 200},
    {"api": "payment", "status": 200},
    {"api": "search", "status": 404},
]


def api_success_rate(logs):
    total_calls = {}
    success_calls = {}

    for log in logs:
        api = log['api']
        status = log['status']

        if api not in total_calls:
            total_calls[api] = 0
            success_calls[api] = 0

        total_calls[api] += 1

        if status == 200:
            success_calls[api] += 1

    result = {}
    for api in total_calls:
        success_rate = (success_calls[api] / total_calls[api]) * 100
        result[api] = round(success_rate, 2)
    return result


print(api_success_rate(logs))

'''used three dictionaries:
one for counting total calls per API,
one for counting successful calls,
and one for storing final success rates.
After processing all logs in O(n) time, I computed success rate as (success / total) * 100 for each API.”'''