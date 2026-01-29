'''
Patterns tell stories in numbers. Your task is to generate a simple sequence of numbers arranged in rows, like filling up seats in a theater one by one, starting from 1 and going upwards.
'''

def generate_theater_pattern(rows):
    pattern = []
    num = 1
    for i in range(rows):
        row = []
        for j in range(i + 1):
            row.append(str(num))
            num += 1
        pattern.append(" ".join(row))
    return "\n".join(pattern)
print(generate_theater_pattern(5))