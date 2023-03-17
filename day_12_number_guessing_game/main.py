from random import randint
from art import logo

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def set_difficulty():
    difficulty = input("Choose a difficulty level. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return EASY_LEVEL_ATTEMPTS
    elif difficulty == "hard":
        return HARD_LEVEL_ATTEMPTS


def check_guess(user_guess, number, attempts):
    if user_guess > number:
        print("Too high.")
        return attempts - 1
    elif user_guess < number:
        print("Too low.")
        return attempts - 1


print(logo)
print("""Welcome to the Number Guessing Game!
I am thinking of a number between 1 and 100.""")


number = randint(1, 100)
attempts = set_difficulty()
print(f"You have {attempts} attempts remaining to guess the number.")
is_attempts_done = False



while not is_attempts_done:
    user_guess = int(input("Make a guess: "))
    attempts = check_guess(user_guess, number, attempts)


    if attempts == 0:
        print("You have run out of guesses, you lose.")
        is_attempts_done = True
    else:
        print(("Guess again."))

    if user_guess == number:
        print(f"You win, the answer was {number}.")
        is_attempts_done = True


