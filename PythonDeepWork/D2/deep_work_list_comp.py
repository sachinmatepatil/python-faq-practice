# List & Dict Comprehensions — short way to build collections
#list comprehension pattern
# [expression for intem in iterable if condition]

#Example 1: Sqaures of even numbers

#Without list comprehension

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = []
for n in nums:
    if n%2 == 0:
        even_squares.append(n*n)
print(even_squares)

#With list comprehension
even_sqaures = [i**2 for i in nums if i%2==0]
print(even_sqaures)

