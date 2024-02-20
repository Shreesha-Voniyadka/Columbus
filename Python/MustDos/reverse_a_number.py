# Python program to reverse a number
n = 1234

# Method 1
reverse = 0
while n!=0:
    reverse = reverse*10 + n%10       
    n = (n//10)
print("After reverse : %d" %reverse) 

# Method 2
n = 1234
rev = int(str(n)[::-1])
print(rev)