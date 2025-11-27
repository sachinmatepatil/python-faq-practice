# Task 1 — OOP Reinforcement (30 min)
# Add these features to yesterday’s Booking class:
# add validation for totalprice > 0
# add method apply_discount(percent)
# add method get_duration() → checkout - checkin (in days)
from doctest import Example

# 🔹 Task 2 — Python Data Structures Practice (30 min)
# Solve these (interview-oriented):
# Two Sum
# Group Anagrams
# Merge Intervals:

#Both task completed in faq task 2 is there and task 1 updated in day1 task


#Task 3 — Advanced Python (60 min)
# Study + implement small examples for:
# Decorators
# Lambda + map/filter
# List/dict comprehensions
# Try/except + custom exception class

# Let's start with Decorators
#Decorator add extra functionality to existing function without modufyin existing function

#Decorator is a function that - takes a function as input - wraps it  with extra code and
#returns new function with extra functionality

#Example: Simple logging decorator

def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned {result}")
        return result
    return wrapper


@log_call
def add(a, b):
    return a + b


@log_call
def greet(name):
    return f"Hello, {name}!"


# Test
add(2, 3)
greet("Sachin")

# @log_call wraps add and greet.
# When you call add(2, 3):
# It prints a log before calling add
# Calls add(2, 3)
# Prints the result

# Decorators are heavily used in:
# Logging
# Authentication
# Retry logic
# Measuring time, etc.