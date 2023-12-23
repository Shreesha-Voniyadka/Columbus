"""
Given an array arr of size N and an element k. 
The task is to find the count of elements in the array that appear more than n/k times.

Input:
    N = 8
    arr = [3,1,2,2,1,2,3,3]
    k = 4
Output: 
    2
Explanation: 
    In the given array, 3 and 2 are the only elements that appears more than n/k times.
"""
def Mysolution(n,k,arr):
    """
    The function `Mysolution` takes in three parameters `n`, `k`, and `arr`, and returns the count of
    elements in `arr` that appear more than `n // k` times.
    
    param n: The parameter `n` represents the total number of elements in the array `arr`
    param k: The value of k determines the threshold for a number to be considered "frequent". In this
            solution, a number is considered frequent if it appears more than n/k times in the array
    param arr: The `arr` parameter is a list of integers
    return: The function `Mysolution` returns the count of elements in the given array `arr` that
    appear more than `n // k` times.
    """
    count = 0
    val = n // k
    stack = {}
    for x in arr:
        # Add to dictinary as 2:3
        if x not in stack:
            stack[x] = 1
        else:
            stack[x] += 1
    for i in stack.values():
        # check value greater than n/3 i.e 2
        if i > val:
            count+=1
    return count

if __name__ == "__main__":
    Mysolution(8,4,[3,1,2,2,1,2,3,3])