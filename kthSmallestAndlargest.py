def kthsmallestandlargest(arr, k ):

    arr.sort()
    n = len(arr)

    kth_smallest = arr[k-1]
    kth_largest = arr[n-k]

    return kth_smallest, kth_largest


arr = [7, 10, 4, 3, 20, 15]
k = 3
print(kthsmallestandlargest(arr, k))