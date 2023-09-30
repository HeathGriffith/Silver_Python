'''
# normal
def show_truth():
    mysterious_var = 'Yay'
    print(mysterious_var)
show_truth()


# can define the variable outside function defintion before the function call
def show_truth():
    print(mysterious_var)
mysterious_var = 'Yay'
show_truth()


# *"shadowing"*: there is already the variable with the name outside the function =>
#   two variables are created. The *local variable* (inside the function) shadows the global variable during function call =>
#       the *global variable* is available before and after the function call
def show_truth():
    mysterious_var = 'New Yay'
    print(mysterious_var)
mysterious_var = 'Yay'
print(mysterious_var)
show_truth()
print(mysterious_var)


# RARE and AVOID: If don't want secondary variable, can change the global variable even outside function body:
def show_truth():
    global mysterious_var = 'New Yay'
    print(mysterious_var)
mysterious_var = 'Yay'
print(mysterious_var)
show_truth()
print(mysterious_var)


# when working with lists (expected)
def show_truth():
    mysterious_var = ['New Yay']
    print(mysterious_var)
mysterious_var = ['Yay']
print(mysterious_var)
show_truth()
print(mysterious_var)
'''

# when working with lists (surprise):
def show_truth():
    mysterious_var.append('New Yay')
    print(mysterious_var)
mysterious_var = ['Yay']
print(mysterious_var)
show_truth()
print(mysterious_var)
# since local variable was not created, the method affects the global variable
# if you assign a new list (or dictionary, but not (immutable) tuples) to the same variable within the function, 
#   shadowing works, but if you change the list using a method ( with '[]' or 'del')