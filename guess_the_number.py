import random

# Choose a random number between 1 and 100
def choose_number():
    number = random.randint(1, 100)
    return number


# Generate the secret number
secret_number = choose_number()

# Ask the player to guess the number
guessed_number = int(input("Guess the number: "))

# Repeat until the player finds the secret number
while guessed_number != secret_number:

    # Check if the guess is too low
    if secret_number > guessed_number:
        print("Too low!")

    # Check if the guess is too high
    elif secret_number < guessed_number:
        print("Too high!")

    # Ask the player to guess again
    guessed_number = int(input("Guess the number: "))

# Display a message when the player wins
print("Congratulations! You found the secret number!")
