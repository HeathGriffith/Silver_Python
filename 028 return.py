'''
def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum/len(input_numbers)
    # notice no parenthese for return
    return average

print('The average is:', get_average([1, 2, 3, 4, 5]))

average = get_average([1, 2, 3, 4, 5])
if average > 2.3:
    print('The average is high')
    

# the keyword *return* does two things at once: (1) gives the result; (2) immediately exits the function =>
#   any statement after return statement will be ignored, e.g. (with no output),

def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum/len(input_numbers)
    return average
    print('prove it')
get_average([2])

# example 1/3 with with populated list:
def is_first_last_equal (number_list):
    if (number_list[0] == number_list[-1]):
        return True
    else:
        return False
print(is_first_last_equal([10, 20, 30, 40, 10]))

# example 2/3 with empty list (index error) 
def is_first_last_equal (number_list):
    if (number_list[0] == number_list[-1]):
        return True
    else:
        return False
print(is_first_last_equal([]))

# exmample 3/3 modification to exit function when no elements in list
'''
def is_first_last_equal(number_list):
    if len(number_list) == 0:
        return
    if (number_list[0] == number_list[-1]):
        return True
    else:
        return False
print(is_first_last_equal([]))
