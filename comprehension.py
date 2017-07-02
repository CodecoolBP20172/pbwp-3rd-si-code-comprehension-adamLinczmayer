import random  # Import module random

guessesTaken = 0  # Assign 0 to guessesTaken variable

print('Hello! What is your name?')  # Print the string on the screen
myName = input()  # Assign user input to myName variable

number = random.randint(1, 20)  # Assign random numbers between 1 and 20 to a variable (number)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  # print the string with myName variable

while guessesTaken < 6:  # Make a loop while gussesTaken variable less than 6
    print('Take a guess.')  # Print the sting
    guess = input()  # Assing a user input to the guess variable
    guess = int(guess)  # Convert the value of guess variable into an integer

    guessesTaken += 1  # Add 1 to guessesTaken variable (in every round of the loop)

    if guess < number:  # If the user input less than a random number (1-20)
        print('Your guess is too low.')  # Print this string

    if guess > number:  # If random number (1-20) less than user input 
        print('Your guess is too high.')  # Print this string

    if guess == number:  # If the user input equal to a random number (1-20)
        break  # Terminate the loop 

if guess == number:  # If the user input equal to a random number (1-20)
    guessesTaken = str(guessesTaken)  # Convert the value of guessesTaken to a string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
    # print the string with myName and guessesTaken variables 

if guess != number:  # If the user input not equal to a random number (1-20)
    number = str(number)  # Convert the value of number into a string
    print('Nope. The number I was thinking of was ' + number)  # print the string with number variable
