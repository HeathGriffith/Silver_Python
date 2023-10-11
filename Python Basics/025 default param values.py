# *sep* and *end* parameters of *print* function are: 
# keyword arguments (or 'named argumets'): always optional; always have default value; always appear after all positional args
# for *print* function, *end* argument has default value of '\n', and *sep*, the default of white space char   
print('Hello', 'How are you?', end='.', sep='-')

# parameters with a default value must appear at the end
def print_letter_count(text, letter='a'):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)

print_letter_count('How many times does does the letter "a" appear here?')

# w/ the following, can invoke function without argument because both parameters have default values
def print_letter_count_2(text = 'this is the string to search', letter='a'):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)

print_letter_count_2 ()

# positional arguments must appear before keywords (named) arguments when call functions, e.g.,
# !X print_letter_count_2(letter='a', 'Search here') !X

