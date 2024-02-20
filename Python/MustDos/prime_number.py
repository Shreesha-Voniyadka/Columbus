# Prime Number Program
n =13
i, t= 0,0 
for i in range(2, n//2):
    if n % i == 0:
        t = 1
        break

if t == 1:
    print("Nope not a Prime")
else:
    print("Yes its a Prime") 