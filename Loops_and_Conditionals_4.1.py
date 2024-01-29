import random

# choosing a number from 1 to 10 to assign variable secret
random = random.randint(1,10)

# Entering the value guess
guess = int(input("Enter your guess! "))

# prints the values
print("The random number was",random)
print("Your guess was",guess)

# If Elif Else statement
if guess < random:
    print('Your guess was too low!')
elif guess > random:
    print('Your guess was too high!')
else:
    print('You guessed it!')
