# bec ditionaries are mutable, can start empty and add elements
grades = {}
grades['John'] = 'A-'
grades['Anne'] = 'B'
print(grades)

# Assume Anne retakes and improves
grades['Anne'] = 'A'
print(grades)

# option two: update method (unnecessary)
grades.update({'John':'A'})
print(grades)

# check number of key-value pairs with 
len(grades)

# check if given key is present with 'in' operator
if 'John' in grades:
    print('John got:', grades['John'])

# to delete entry
del grades ['John'] 
print(grades)

# iterate a dictionary (dictionaries are ordered collections)

# (1) to see only keys in output
for element in grades:
    print(element)
# or 'for elemements in grades.keys():' same output

# (2) to see only values in ouput
for element in grades.values():
    print(element)

# (3) to get access too both keys and values, use two control variables separated by a comma:
for person, grade in grades.items():
    print(person, 'got an', grade) 

