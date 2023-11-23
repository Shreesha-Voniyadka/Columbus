#Sliding window
# Input  : arr[] = {100, 200, 300, 400}, k = 2
# Output : 700

# Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}, k = 4 
# Output : 39
# We get maximum sum by adding subarray {4, 2, 10, 23} of size 4.

# Input  : arr[] = {2, 3}, k = 3
# Output : Invalid
# There is no subarray of size 3 as size of whole array is 2.

# start & end of sliding window: |start-> ... end->|
# short version of sliding window, focus on two pointers
""" This is very important concept please take this carefully """

def max_subarray_sum(arr, k):
    n = len(arr)
    if n < k:
        return "Invalid input"

    max_sum = float('-inf')
    window_sum = sum(arr[:k])

    for i in range(n - k + 1):
        max_sum = max(max_sum, window_sum)
        if i + k < n:
            window_sum = window_sum - arr[i] + arr[i + k]

    return max_sum

# Example usage:
array = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
k = 3
result = max_subarray_sum(array, k)
print("Maximum sum of a subarray of size", k, ":", result)