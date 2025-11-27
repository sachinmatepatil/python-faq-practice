from tkinter.font import names

#DEcorator example
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with arg {args} and kwargs {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

@log_decorator
def calculate_tax(value_per):
    tax_rate = 0.07
    return value_per * tax_rate

calculate_tax(500)


#Converting list of strings to upper case
list_strings = ['apple', 'banana', 'cherry', 'date']
upper_case_list_string = list(map(lambda x:x.upper(),list_strings))
print(upper_case_list_string)

#Filtering name starting with "S"
names = ['Sam', 'John', 'Sara', 'Mike', 'Sophie']
start_with_s = list(filter(lambda x:x[0] == 'S',names))
print(start_with_s)

#list of squares
no = [1,4,10,20,5]
square_list = [i*i for i in no]
print(square_list)

#dict number odd,even
num = [1,2,3,4,5,6,7,8]
dict_odd_even={i:('even' if i%2==0 else 'odd') for i in num}
print(dict_odd_even)

#create custome exceptio for NegativeNumberError and raise if for negative inputs

class NegativeNumberError(Exception):
    """Custom exception for negative inputs."""
    pass

def check_number(num):
    if num<0:
        raise NegativeNumberError("Negative numbers are not allowed.")
    else:
        return f"{num} is a valid number."

num = [10,20,50,-60,20,-9]
for i in num:
    try:
        x = check_number(i)
        print(x)
    except NegativeNumberError as e:
        print(f"{i}",e)
