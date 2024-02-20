# Fibonacci series program in python
# Method 1
n = 5
f,s = 0,1
for i in range(0,n):
    if i <=1 :
        result = i
    else:
        result = f +  s
        f = s
        s = result
    print(result)

# Method 2
n = 5
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return(fib(n-1)+fib(n-2))

for i in range(0, n):
    print(fib(i))

     