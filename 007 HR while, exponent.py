# wrong order
n = int(input())
while n > 0:
    n -= 1
    print(n**2)

# *** Three Ways ***

#1 for loop
n = int(input())
for i in range(0, n):
    print(i**2)

#2 reversed while logic
n = int(input())
i = 0
while i < n:
    print(i**2)
    i += 1

#3 use a list
n = int(input())
squared_numbers = []

while n > 0:
    n -= 1
    squared_numbers.append(n**2)

for square in reversed(squared_numbers):
    print(square)