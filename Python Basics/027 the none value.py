# Functions either cause an effect (*print*) or return a value (*len*) or both (*input*)
# *None* refers to a special value -- no value (not 0, not True or False, not an empty string)


'''
# *print* and the *user-defined function* 'greet()' lack specific return values -- None is returned =>
#    though not displayed for *print* normally 
print_return = print('Hello')
print(print_return)

def greet():
    print('Hello')
x = greet()
print(x)
'''
x = None
if x:
    print("None is True")
elif x is False:
    print("None is False")
else:
    print("None is not True or False") 

y = None
if y is None:
    print('yes')
if y == None:
    print('still yes')
