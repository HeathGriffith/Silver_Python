# assertions are assumptions (always true) in program

def calculate_inverse(number):
    assert (number != 0), 'Got 0 as number!'
    return 1/number

calculate_inverse(0)

# can be added at beginning of function to ensure correct data received or indicate to other develeopers
# don't use to invalidate user input (bec possible to turn off assertions when publish code)
# catch and fix bugs in development -- not for error handling (no try/except assertion-error blocks)