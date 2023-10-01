value = int(input('enter an integer: '))
print('the inverse of', value, 'is', 1/value)

# a *ValueError* if a non-integer is supplied.
# possible fix:
try:
    value = int(input('enter an integer: '))
    print('the inverse of', value, 'is', 1/value)
except: 
    print("That wasn't an integer.")

# problem is that there might be a different error, a *ZeroDivisionError*:
try:
    value = int(input('enter an integer: '))
    print('the inverse of', value, 'is', 1/value)
except ValueError: 
    print("That wasn't an integer.")
except ZeroDivisionError:
    print("You can't divide by zero.")
# final except block to catch anything not anticipated
except:
    print("something went wrong.")

# you can specify as many exceptions as needed, but each can only be specified once