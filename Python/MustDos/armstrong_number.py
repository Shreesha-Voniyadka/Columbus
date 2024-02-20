# Armstrong number program in python
# 153 = 1^3 + 5^3 + 3^3
# 1634 = 1^4 + 6^4 + 3^4 + 4^4
n = 153

# Method 1
temp = n
suma = 0
count = len(str(n))
while temp > 0:
    digit = temp % 10
    suma += digit ** count
    temp //= 10
if n == suma:
    print("yes")
else:
    print("No")

# Method 2
n = 153
digits = [int(digit) for digit in str(n)]
count = len(digits)
sume = sum([digit ** count for digit in digits])
if sume == n:
    print("yes")
else:
    print("no")
