# Python program for palindrome
n = 121
r ,t = 0, n 
while t != 0:
    r = r * 10 + t % 10
    t = t // 10
if r == n:
    print("Yes")
else:
    print("Nope")

    # Method 2 

num = 131
def reverse(num):
    if num < 10:
      return num
    else:
      return int(str(num % 10) + str(reverse(num//10)))


def isPalindrome(num):
    if num == reverse(num):
        return 1
    return 0


if isPalindrome(n) == 1:
    print("Given number is a palindrome")
else:
    print("Given number is a not palindrome")
