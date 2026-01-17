'''Problem Statement
On a cold winter day, you want to convert temperatures from Celsius to Fahrenheit to understand the weather better. Using the formula F = (C × 9/5) + 32, you decide to implement a program that performs this conversion for any given Celsius temperature.'''

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

if __name__ == "__main__":
    c=0
    f = celsius_to_fahrenheit(c)
    print(f)