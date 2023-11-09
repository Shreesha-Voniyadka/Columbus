"""
    Question :  Given a string S, check if it is palindrome or not. 
    Difficulty  : Easiest
    Solution : 
        My method in case of python : just reverse the string check both are same

"""

test_string = input("Enter string to check =====>  ")

if test_string == test_string[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")