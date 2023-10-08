'''
mini-project 1: Create a given number of random EC2-instance names based on given department.
'''

# Importing necessary libraries for randomness and string manipulation
import random
import string

# Get user input for number of EC2 instances they want to name
EC2_quantity = int(input("How many EC2 instance names are needed? "))

# Get user input for department name, which will be used in the EC2 name
EC2_dept = input("What department will these EC2 instances be in: Marketing, Accounting, or FinOps? ")

# Convert department name to lowercase to handle varied case inputs
EC2_dept_meant = EC2_dept.lower()

# Loop until a valid department name is provided
while EC2_dept_meant != "marketing" and EC2_dept_meant != "accounting" and EC2_dept_meant != "finops":
    EC2_dept = input("If that's right, you shouldn't use this generator.\nOtherwise, what department will these EC2 instances be in: Marketing, Accounting, or FinOps?")
    EC2_dept_meant = EC2_dept.lower()

# Create a pool of characters (lowercase letters + digits) for random name generation
randomizing_options = string.ascii_lowercase + string.digits

# Loop to generate and print the unique EC2 names based on user input
for element in range(1, EC2_quantity + 1):
    EC2_name = EC2_dept_meant + '.' + ''.join(random.choice(randomizing_options) for option in range(7))
    print(EC2_name)
