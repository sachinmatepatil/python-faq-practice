'''
Problem Statement
Imagine you are on a quest to find the treasure hidden among numbers. This treasure is the sum of all odd numbers that lie between two points on the number line. Given a range, your task is to gather all these odd numbers and calculate their total sum. Can you write a program that helps you uncover this hidden treasure?
'''



ranges = [10, 10]


def sum_hidden_treasure(ranges):
    total = 0
    for i in range(ranges[0], ranges[1] + 1):
        if i % 2 != 0:
            total += i
    return total


print(sum_hidden_treasure(ranges))