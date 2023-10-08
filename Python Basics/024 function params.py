'''
# turn following code block into function

input_numbers = [5.0, 3.5, 7.8, 9.9, 10.0]
sum = 0.0
for number in input_numbers:
    sum += number
average = sum / len(input_numbers)
print(average)

# element in paratheses = parameter: 
# (1) variable defined in the parentheses after the function name
# (2) only exists inside function

def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    print(average)

# elsewhere in code, invoke/call the value for the parameter
get_average([5.0, 3.5, 7.8, 9.9, 10.0])
# above, the list is the argument, and the value of the argument is assigned to the parameter named input numbers


# e.g. 2, function that takes two parameters: string and letter, to count number of times letter appears
def print_letter_count(text, letter):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print(letter, 'appears', counter, 'times')

# note the order of arguments matters (= 'positional arguments')
print_letter_count('Welcome little one', 'e')

# named arguments are less frequent, but allowed
print_letter_count(text='Welcome', letter='e')
print_letter_count(letter='e', text='Welcome')
'''