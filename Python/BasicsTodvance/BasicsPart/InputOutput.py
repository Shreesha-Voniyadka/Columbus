""" 
Input and Output in Python. 
"""
"""
"""
# Input Syntax : 
variable_name = input('STATEMENT') # Single Input
variable_name = datatype(input('STATEMENT')) # Single Input

# For list
lst = [] 
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)

variable_name = raw_input('STATEMENT') 
input().split(separator, maxsplit) # Multiple Inputs, can also use list comprehension

# Output Syntax
print(value(s), sep= ' ', end = '\n', file=file, flush=flush)
print(variable_name)
print(variable_name,end='')
print(*variable_name)
print(type(variable_name)) # To print type of variable - int, float, bool....
"""
Notes: Whatever you enter as input, the input function converts it into a string. if you enter an integer value still input() function converts it into a string. 
You need to explicitly convert it into an integer in your code using typecasting. Eg :  num1 = int(input())
"""
# ===============================================================================================================================
""" Examples """
name = input('What is your name?\n')     # \n ---> newline  ---> It causes a line break

g = raw_input("Enter your name : ")

num1 = int(input())              # Typecasting

a, b = input("Enter two values: ").split()

# taking multiple inputs at a time 
# and type casting using list() function
x = list(map(int, input("Enter multiple values: ").split()))
# taking two input at a time list comprehension
x, y = [int(x) for x in input("Enter two values: ").split()]

print("Hello, my name is", name, "and I am", age, "years old.")

print ("GeeksForGeeks is the best platform for DSA content", end= "**")
#output : GeeksForGeeks is the best platform for DSA content**Welcome to GFG

print('09','12','2016', sep='-') 
# output : 09-12-2016


""" Output Formatting """
# %[flags][width][.precision]type 
print("Geeks : %2d, Portal : %5.2f" % (1, 05.333)) 
print("Total students : %3d, Boys : %2d" % (240, 120))   # print integer value
print("%7.3o" % (25))   # print octal value
print("%10.3E" % (356.08977))   # print exponential value
# Output : Geeks :  1, Portal : 5.33
#          Total students : 240, Boys : 120
#          031
#          3.561E+02

#
print('I love {} for "{}!"'.format('Geeks', 'Geeks'))
# using format() method and referring a position of the object
print('{0} and {1}'.format('Geeks', 'Portal'))
print('{1} and {0}'.format('Geeks', 'Portal'))
print(f"I love {'Geeks'} for \"{'Geeks'}!\"")
# using format() method and referring a position of the object
print(f"{'Geeks'} and {'Portal'}")
# Output: I love Geeks for "Geeks!"
# Geeks and Portal
# Portal and Geeks
# I love Geeks for "Geeks!"
# Geeks and Portal 