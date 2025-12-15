arr = [3,2,3]

def missing_and_repeating_in_arr(arr):
    n=len(arr)

    freq = {}
    for num in arr:
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1

    missing = -1
    repeating = -1

    for i in range(1, n+1):
        if i not in freq:
            missing = i
        elif freq[i] > 1:
            repeating = i
    return (repeating,missing )

print(missing_and_repeating_in_arr(arr))