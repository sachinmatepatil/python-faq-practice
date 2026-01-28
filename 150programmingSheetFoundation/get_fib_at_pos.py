'''In the world of sequences, the Fibonacci series is legendary, starting with 0 and 1, each number being the sum of the two before it. Your challenge is to find the Fibonacci number sitting at a specific position in this endless chain. Can you pinpoint the exact number that belongs there?'''
def get_fib_at(n):
    if n==0: return 0
    if n==1: return 1

    prev, curr = 0, 1
    for num in range(2,n+1):
        prev,curr=curr,prev+curr
    return curr

print(get_fib_at(0))
print(get_fib_at(1))
print(get_fib_at(3))

#Time Complexity: O(n) - single loop running
#space Complexity: O(1) - constant space used