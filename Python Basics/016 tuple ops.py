# len function to count elements in tuple
user_data = ('John', 'American', 1964)
print(len(user_data))

# *in* and *not in* operators work same as in lists
user_data = ('John', 'American', 1964)
if 'American' in user_data:
    print("this person is from the USA.")

# can iterate with a for loop
user_data = ('John', 'American', 1964)
for element in user_data:
    print(element)

# can be added or multipled by an integer
user_data2 = ('John', 'American', 1964) + ('teacher',)
print(user_data2)

'''
while *lists* are used with elements of same data types, e.g., male names or float temperatures,
use *tuples* 
(1) with different data types that are related
(2) to perform some operations quicker. E.g., swap value of two variables:
first = 5
second = 7
first, second = second, first

'''
