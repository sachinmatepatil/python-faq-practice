def checkEvenOdd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "Odd"


num = int(input('Enter a number to check'))
x = checkEvenOdd(num)
print(x)
