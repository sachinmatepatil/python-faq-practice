'''
Problem Statement
Legend says that certain numbers hold a self-loving property—equal to the sum of the cubes of their digits. Find all such 'Armstrong numbers' within a given range.
'''
'''
Examples
Input:
range = [1, 500]
Output:
[1, 153, 370, 371, 407]
'''
#Method 1
# def find_armstrong_numbers(start,end):
#     armstrong_num = []
#
#     for i in range(start,end+1):
#         power = len(str(i))
#         temp = i
#         sum_of_powers = 0
#
#         while temp>0:
#             digit = temp%10
#             sum_of_powers += digit ** power
#             temp //=10
#
#         if sum_of_powers == i and i!=0:
#             armstrong_num.append(i)
#     return armstrong_num
#
# # Example usage:
# start = 1
# end = 500
# result = find_armstrong_numbers(start,end)
# print(result)

#Method 2
def find_armstrong_numbers_v2(start,end):
    armstrong_num = []

    for i in range(start,end+1):
        power = len(str(i))
        num_str = str(i)
        if sum(int(digit) ** power for digit in num_str) == i:
            armstrong_num.append(i)
    return armstrong_num
# Example usage:
start = 1
end = 500
result = find_armstrong_numbers_v2(start,end)
print(result)