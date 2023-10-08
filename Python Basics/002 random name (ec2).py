import random
import string
EC2_quantity = int(input("How many EC2 instance names are needed? "))
EC2_dept = input("What department will these EC2 instances be in: Marketing, Accounting, or FinOps? ")
EC2_dept_meant = EC2_dept.lower()
while EC2_dept_meant != "marketing" and EC2_dept_meant != "accounting" and EC2_dept_meant != "finops":
    EC2_dept = input("If that's right, you shouldn't use this generator.\nOtherwise, what department will these EC2 instances be in: Marketing, Accounting, or FinOps?")
    EC2_dept_meant = EC2_dept.lower()
randomizing_options = string.ascii_lowercase + string.digits
for element in range (1, EC2_quantity + 1):
    EC2_name = EC2_dept_meant + '.' + ''.join(random.choice(randomizing_options) for option in range(7))
    print(EC2_name)