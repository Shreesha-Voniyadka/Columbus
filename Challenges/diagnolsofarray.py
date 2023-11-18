#!/bin/python3
#  Get the sum of diagnols.... Forget about the inputs just see the logic
# Basicaly from right diagnol just have to use i+j == n-1 only square matrix tho
import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    suml = 0
    sumr = 0
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if i==j:
                suml = suml + arr[i][j]
            if (i+j) == (n-1):
                sumr = sumr + arr[i][j]
    return abs(sumr-suml)
    
if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)



