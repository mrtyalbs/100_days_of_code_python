from game_data import data
from art import logo, vs
from random import choice
import os

# Clear console function
clear = lambda: os.system('cls')

# Format the data into printable format function
def format_data(data):
    """Takes the data and returns data into printable format."""
    return data["name"] + ", " + data["description"] + ", " + data["country"] + "."


# Check if user is correct

def check_guess(guess, follower_count_a, follower_count_b):
    """This function checks is user correct."""
    if follower_count_a > follower_count_b:
        return guess == "a"             # if guess = a return True else return False
    else:
        return guess == "b"             # if guess = b return True else return False

# Display logo.
print(logo)

# User score
score = 0

game_continue = True
account_b = choice(data)

# Make game repetable
while game_continue:
    # Generate a random data from game_data. Making account at position B become the next account at position A.
    account_a = account_b
    account_b = choice(data)

        # Check datas are equal
    if account_a == account_b:
        account_b = choice(data)

    # Format the data into a printable format.

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask user for a guess.
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Get follower count
    follower_count_a = account_a["follower_count"]
    follower_count_b = account_b["follower_count"]

    # Check the users guess
    is_correct = check_guess(user_guess, follower_count_a, follower_count_b)

    # Clear the screen
    clear()
    # Give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You are right, your current score is {score}. ")
    else:
        game_continue = False
        print(f"You are wrong, your final score is {score}. ")

