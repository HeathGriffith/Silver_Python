# Start an infinite loop that will keep running until it's explicitly broken out of
while True:
    # Prompt the user to enter a guess for the release year of Python 1.0, and convert the input to an integer
    guess = int(input("When was Python 1.0 released? "))
    # Check if the guessed year is greater than 1994
    if guess > 1994:
        # If the guess is greater than 1994, inform the user that the actual year is earlier and prompt them to guess again
        print("It was earlier than that!")
    # Check if the guessed year is less than 1994
    elif guess < 1994:
        # If the guess is less than 1994, inform the user that the actual year is later and prompt them to guess again
        print("It was later than that!")
    # If the guessed year is neither greater than nor less than 1994, it must be equal to 1994
    else:
        # If the guess is correct (1994), congratulate the user and break out of the loop to end the program
        print("Correct!")
        break