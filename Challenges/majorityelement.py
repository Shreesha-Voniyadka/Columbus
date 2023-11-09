'''
Source: GeeksforGeeks
Given an array A of N elements. Find the majority element in the array. 
A majority element in an array A of size N is an element that appears strictly more than N/2 times in the array.

'''

def majorityelement(a,n):
    for x in a:
        if x in n:
            d[x] += 1
        else:
            d[x] = 1
        if d[x] > n//2:
            return d[x]
    return -1 

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
    T=int(input())
    while(T>0):
        N=int(input())  
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.majorityElement(A,N))        
        T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends