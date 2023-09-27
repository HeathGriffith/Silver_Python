'''
first = input("Enter first number: ")
second = input("Enter second number: ")
temporary = first = second
second = temporary


# shortcut
first = input("Enter first number: ")
second = input("Enter second number: ")
print("before swapping: ", first, second)
first, second = second, first
print("after swapping: ",first, second)
'''

# with lists
top_cities = ['NYC', 'LA', 'Singapore', 'Chicago', 'Houston', 'Phoenix']
top_cities[0], top_cities[4] = top_cities[4], top_cities[0]
print(top_cities)

#alpha or numerical sorting with the method .sort() and reversed
random_numbers = [2, 5, 0, -3, 4]
random_numbers.sort(reverse=True)
print(random_numbers)

# .sort() is a method: changes the list; can't be undone easily. For temporary sort: list function instead of method
fruits = ['apple', 'pear', 'banana', 'orange', 'plum']
print(sorted(fruits))
print(fruits)