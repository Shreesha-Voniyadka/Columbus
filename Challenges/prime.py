"""
For a given number N check if it is prime or not. 
A prime number is a number which is only divisible by 1 and itself.
Still in doubt need to see more got time complexity issue
"""
import math
def Mysolution(N):
    if N <= 1:
            return 0
    root =int(math.sqrt(N))
    for i in range(2, root+1):
        if N % i == 0:
            return 0

    return 1

if __name__=="__main__":
    Mysolution(25)