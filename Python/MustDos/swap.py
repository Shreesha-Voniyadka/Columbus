# Python program to swap two number without using third variable
# Method 1
a = 10
b = 20
a = a-b
b = a+b
a = b-a
print("After swapping")
print("value of a is : ", a)
print("value of b is : ", b)

# Method 2 using third variabble
a,b = 10,20
tempvar = a
a = b
b = tempvar
print("After swapping")
print("value of a is : ", a)
print("value of b is : ", b)

# Method 3 
a, b = 10, 20
a , b = b , a
print("After swapping")
print("value of a is : ", a)
print("value of b is : ", b)
