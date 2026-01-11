def kthsmallestandlargest(arr, k ):

    arr.sort()
    n = len(arr)

    kth_smallest = arr[k-1]
    kth_largest = arr[n-k]

    return kth_smallest, kth_largest
#Time complexity: O(n log n) due to sorting
#space complexity: O(1) if we ignore the input array space or o(n) if we consider the input array space

arr = [7, 10, 4, 3, 20, 15]
k = 3
print(kthsmallestandlargest(arr, k))

# Method 2: Using heap
import heapq

def kthsmallestandlargest_heap(arr, k):
    kth_smallest = heapq.nsmallest(k, arr)[-1]
    kth_largeest = heapq.nlargest(k, arr)[-1]

    return kth_smallest, kth_largeest
#Time complexity: O(n log k)
#space complexity: O(k)
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(kthsmallestandlargest_heap(arr, k))

'''Heap-based solution (bullet points)
	•	heapq provides a min heap implementation in Python
	•	We use heap because it helps find top k elements efficiently

⸻

heapq.nsmallest(k, arr)
	•	Returns the k smallest elements from the array
	•	Internally maintains a heap of size k
	•	Avoids sorting the entire array
	•	Output is a list of k smallest elements (sorted)
	•	The last element of this list is the kth smallest

⸻

heapq.nlargest(k, arr)
	•	Returns the k largest elements from the array
	•	Uses a heap of size k internally
	•	Output is a list of k largest elements (sorted in descending order)
	•	The last element of this list is the kth largest

⸻

Why this works
	•	We only care about k elements, not the full array
	•	Heap keeps track of relevant elements efficiently

⸻

Complexity
	•	Time: O(n log k)
	•	Space: O(k)

⸻

When to use this approach
	•	Large arrays
	•	Small k
	•	When optimization is required

⸻

Final takeaway (one-liner)

Heap allows us to find kth smallest and kth largest without sorting the entire array, improving performance.
'''