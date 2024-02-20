# Perfect number program in Python
# A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.


n = 6
s = 0
for i in range(1,(n//2)+1):
    r = n % i
    if r == 0:
        s = s + i
if s == n:
    print("yes") 
else:
    print("nope") 
