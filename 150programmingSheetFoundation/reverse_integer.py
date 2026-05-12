# Reverse an Integer: Reverse the digits of an integer (handle negative numbers and overflow).

def reverse_integer(x):
    sign = -1 if x < 0 else 1

    x = abs(x)

    rev = 0

    while x != 0:
        digit = x % 10
        rev = rev * 10 + digit
        x = x // 10

    rev *= sign

    # 32-bit overflow check
    if rev < -2**31 or rev > 2**31 - 1:
        return 0

    return rev


print(reverse_integer(12345))
print(reverse_integer(-123))
#
# Uses mathematical operations:
#
# * %10 → get last digit
# * //10 → remove last digit
# Time complexity -  O(log n)
# space complexity - 0(1)

# I repeatedly extract the last digit using modulo, append it to the reversed number,
# and remove the last digit using integer division. I also handle sign and overflow conditions.