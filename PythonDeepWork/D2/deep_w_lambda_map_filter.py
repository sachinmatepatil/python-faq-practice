#1 Lambda
#Lambda = small anonymous function

#Example of normal function
def square(x):
    return x * x

#Lambda version - same thing but shorter
square = lambda x : x * x

#Example 1 : map with lambda(transform all items in a list)

nums = [1, 2, 3, 4, 5]

square_nums = list(map(lambda x: x * x, nums))
print(square_nums)  # Output: [1, 4, 9, 16

#Map - applies the function to every item
#lambda - x: x*x -> small function that returns square of x

#Example 2: filter with lambda (filter items in a list or keep only those that satisfy a conition
nums = [1, 2, 3, 4, 5]

even_nums = list(filter(lambda x: x % 2==0, nums))
print(even_nums)

#filter - keeps only items that satisfy the condition
#lambda - x: x % 2==0 -> small function that returns True if x is even

#Tip:For readability, in real projects many devs prefer list comprehensions instead of map/filter with lambda.

