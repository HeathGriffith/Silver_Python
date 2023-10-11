# using a loop
numbers = []
for i in range(1, 101):
    numbers.append(i)
print(numbers)

# using a comprehension; note control variable name has to be in front of loop
numbers = [i for i in range(1, 101)]
print(numbers)

# skipping numbers divisible by 3
numbers = [i for i in range(1, 101) if i % 3 != 0]
print(numbers)
