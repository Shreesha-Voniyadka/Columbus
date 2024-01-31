def fib(n):
    """
    The function fib prints/returns the fibainacci result value of n.
    
    param n: The parameter `n` in the `fib` function represents the number of terms in the Fibonacci
    sequence that you want to generate
    """
    res = []
    x = 0
    y = 1
    while n > 0:
        x,y = y,x+y
        res.append(x)
        n-=1
    return res
if __name__ == "__main__":
    fib(5)