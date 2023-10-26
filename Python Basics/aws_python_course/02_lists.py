# starting list
fruits = ["apple", "banana", "orange"]

# print specific element
print(fruits[2])

# find length of list
print(len(fruits))

# return the second-to-last value
print(fruits[-2])

# add to the end
fruits.append("kiwi")
print(fruits)

# add element as third item
fruits.insert(2, "mango")
print(fruits)

# built-in fuction `sorted()` doesn't affect the argument (e.g., the list "fruit")
print(sorted(fruits))
print(fruits)

# but the `.sort()` method does (as methods typically do):
fruits.sort()
print(fruits)

# .reverse() method reverses order (but can invoke it again to go back)

#delete an second element
del fruits[1]
print(fruits)

# the .pop() method (with or without index value) to use a value after removing it
favorite_fruit = fruits.pop(-1)
print(favorite_fruit)

# can remove elements by value with `.remove` method
fruits.remove("apple")
print(fruits)