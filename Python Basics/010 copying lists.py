'''
# variables independent strings, integers, booleans
name_original = 'John Snow'
name_new = name_original
name_original = 'Tom'
print(name_original, name_new)

# different rule for lists (name of list is name of memory location [reference] of list, not list)
list_original = [1, 2, 3]
list_new = list_original
list_original[0] = -5
print('original:', list_original, '\nNew:', list_new)

# how make a copy: slicing (seperate memory location)
list_original = [6, 7, 8]
list_new = list_original[:]
list_original[0] = -5
print('original:', list_original, '\nNew:', list_new)

# copy, e.g., two first elements from list with slicing
list_original = [11, 12, 13]
list_new = list_original[:2]
list_original[0] = -5
print('original:', list_original, '\nNew:', list_new)
'''