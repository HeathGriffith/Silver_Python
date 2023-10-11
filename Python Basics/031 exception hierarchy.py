# SystemExit: immediately terminate program with sys.exit()
# *import sys* necessary 
import sys
user_name = input("Name: ")
if user_name == '':
    print("Can't work with empty name -- closing program.")
    sys.exit()
print("Hello,", user_name)
print("Let's get started . . . ")

# *Exception* examples for beginners
# (A) ArithmeticError
#   (1) ZeroDivisionError

# (B) LookupError (collections such as (1) lists and (2) dictionaries)
#   (1) IndexError (attempt to access element out of range)
#   (2) KeyError (attempt to access nonexistent key)

# (C) TypeError (incorrect variable type, e.g., add string to integer)
age = input("What's your age: ")
print("In ten years, you'll be", age + 10)

# (D) ValueError (variable type correct, but content not correct)
age = int(input("What's your age: "))
# error if a letter is provided




