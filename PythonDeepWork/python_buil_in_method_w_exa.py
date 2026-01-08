# len - length
li = [1, 2, 3, 4, 5, 6]
print(len(li))

# type - check data type
li = [1, 2, 3, 4, 5]
print(type(li))

print(type(10))
print(type({'a': 10}))

# range - sequence of numbers
for i in range(5):
    print(i)

# input - user input
# name = input('Enter username')
# print(name)

# int(), float(), str() - type conversion
print(int('10'))
print(float('10.5'))
num_str = str(100)
print(num_str)

# abs - absolute value
print(abs(-10))

# Max/Min
print(max(1, 23, 241, 2))
print(min(9237, 234, 123))

# Sum
print(sum([1, 2, 3]))

# sorted
n = [43, 34, 4, 2, 34, 5, 234]
sortdd = sorted(n)  # it doesn't modify original
print(sortdd)

# sort
li = [2, 34, 5, 34, 13, 897, 3]
li.sort()
print(li)  # it modifies original

# Enumerate() - index + value
names = ['sachin', 'aditi']
for i, name in enumerate(names):
    print(i, name)

# Zip() - combine iterables
names = ['sachin', 'aditi']
age = [30, 29]

for n, a in zip(names, age):
    print(n, a)

# reversed() and reverse - reverse iterator
s = [1, 2, 3]
s.reverse()
print(s)

s = [98, 342, 3]
list(reversed(s))
print(s)

# all() - all True?
all([True, True, False])  # false

# any() - any True?
any([False, False, True])  # True

# map() - transform item
num = [1, 2, 3, 4, 5]
sq_num = list(map(lambda x: x * 2, num))
print(sq_num)

# filter() - select items
num = [2, 3, 13, 2312, 23, 1, 2, 3]
eve_num = list(filter(lambda x: x % 2 == 0, num))
print(eve_num)

# isinstance() - safe type check
print(isinstance(10, int))
print(isinstance('sac', list))
# prefer over type() in interviews

# dict.get() - safe access
dic = {'name': 'sachin', 'age': 30, 'lang': 'python'}
print(dic.get('name'))
print(dic.get('c', 0))  # 0(no keyerror)

# set - it will give unique values
num = [1, 2, 3, 4, 5, 56, 4, 2, 12, 32, 1]
uniq = set(num)
print(uniq)

# open() - file handling
# with open('sample.txt','w') as f:
#     f.write('Hello world')

# round() - rounding of the value
print(round(2.1231232, 2))

# id() - memory identity
x = 10
print(id(x))

# help()/dir() - introspection
print(help(list))
print(dir(dict))

# more example of:
# enumerate
# all
# any