""" 
    Question : Given an array arr of distinct elements of size N, the task is to rearrange the elements of the array 
               in a zig-zag fashion so that the converted array should be in the below form: 
               arr[0] < arr[1]  > arr[2] < arr[3] > arr[4] < . . . . arr[n-2] < arr[n-1] > arr[n].
    Difficulty : Easy
    Solution : checking corresponding numbers whether number is greater or lesser

"""

arr = input("Enter array ====> ")
N = input("Number of elements of array ====> ")
flag = True
for i in range(n - 1):
    if flag:
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    else:
        if arr[i] < arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    flag = not flag