 # 1 difference between list and tuple in python

# lists = [1,2,3,4,5] #mutable
# tuples = (1,2,3,4,5) #Immutable

# 2 What are pythons built-in data types?
#Numbers, Strings, dictionary, list, tuple, boolean, arithmetic, set, frozenset
# dicts = {'key':'values','name':'sachin','age':24}
# sets = (1,2,3,4,5)
# frozenset = frozenset((1,2,3,4,5))
# strings = 'sachin'
# booleans = True
# numb = 123
# arithmetic = 10 + 5
# list = [1,2,3,4,5]
# tuple = (1,2,3,4,5)

#How do you implement inheritance and super keyword in python?

#how to read and write a file in python?

# with open('sample.txt','w') as f:
#     f.write(str(lists))
#     with open('sample.txt','r') as f:
#         contents = f.read()
#         print(contents)

#What are fixture in Pytest? when they are used?
'''Fixtures in pytest are functions that setup test environments before a test runs and 
clean up afterward.
They help manage test dependencies, setup, teardown and reusable data across multiple test cases.

Key features of pytest fixtures:
1.Reusability: Define once, use in multiple tests.
2.Automatic setup and teardown: Handles pre-test and post-test actions.
3.Scope control: Can be scoped to per function, per class, per module, or per session.
4.Dependency injection: Pass fixtures as test function arguments.
5.Parameterization: Run tests with different fixture values.
'''

# import pytest
#
# @pytest.fixture
# def sample_data():
#     print('\nSetup: Preparing sample data')
#     data = {'name':'sachin','age':30}
#     yield data
#     print('cleanup: Teardown after test')
#
# def test_sample_data(sample_data):
#     assert sample_data['name'] == 'sachin'
#     assert sample_data['age'] == 30
#     print('Test executed with sample data')

'''What is lambda in Python? how it is applied to between map, filter

# Lambda functions are small anonymous functions defined using the lambda keyword.
# They can take any number of arguments but can only have a single expression.
# Lambda functions are often used with higher-order functions like map() and filter().
# Example of lambda with map

x = 50
square_num = lambda x: x ** 2
print(square_num(x))

numbers = [1, 2, 3, 4, 5]

square_num = list(map(lambda x: x**2, numbers))
print(square_num)

even_num = list(filter(lambda x:x %2==0, numbers))
print(even_num)
'''

'''How to sort list in python'''
li = [5,2,9,1,5,6]

li.sort()
print(li)

li_sorted = sorted(li)
print(li_sorted)

''' is python sync or async? explain'''
# Python supports both synchronous and asynchronous programming.
# Synchronous programming executes code sequentially, while asynchronous programming allows for concurrent execution using async/
# await keywords and libraries like asyncio.

'''What is self in python?'''
# In Python, self refers to the instance of the class and is used to access variables and methods associated with that instance.
# It is the first parameter of instance methods in a class.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

"""Difference between classmethod, staticmethod and instance method in python?"""
# Instance Method: The most common type of method, which takes self as the first parameter and operates on instance data.
# Class Method: Takes cls as the first parameter and operates on class-level data. Defined using @classmethod decorator.
# Static Method: Does not take self or cls as the first parameter and does not operate on instance or class data. Defined using @staticmethod decorator.
class MyClass:
    class_variable = "I am a class variable"

    def instance_method(self):
        return "I am an instance method"

    @classmethod
    def class_method(cls):
        return f"I am a class method accessing: {cls.class_variable}"

    @staticmethod
    def static_method():
        return "I am a static method"

obj = MyClass()
print(obj.instance_method())
print(MyClass.class_method())
print(MyClass.static_method())


'''What is use of conftest.py in pytest?'''
# conftest.py is a special configuration file in pytest that allows you to define fixtures, hooks, and other configurations that can be shared across multiple test files in a directory.
# It helps in organizing and reusing test setup code.
# Example of conftest.py
# import pytest
# @pytest.fixture
# def sample_data():
#     return {'name':'sachin','age':30}
# This fixture can then be used in any test file within the same directory or subdirectories.

'''How do you execute only failed test cases in pytest?'''
# pytest --last-failed

'''How do you apply a custom marker in pytest?'''
# You can define a custom marker in pytest by using the @pytest.mark decorator above your test
# For example:
# import pytest
#
# @pytest.mark.sanity
# def test_example():
# assert True
#
# pytest -m sanity


"""how to handle exceptions in python?"""
# Exceptions in Python can be handled using try-except blocks.
# Example:
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print(f"Result is {result}")
finally:
    print("Execution completed.")
