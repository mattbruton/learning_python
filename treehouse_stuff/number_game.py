import random
import re

# Generate random number between 1 and 10.
# Get number guess from player.
# Compare guess to generated number.
# Print if correct/incorrect.

text_border = '=' * 40
instructions = """{0}
I have selected a number between 1 and 10!
Guess my number correctly, and win!
{0}""".format(text_border)

def handle_correct_guess(guess):
    print('Yay! You guessed {}, that was the secret number! Goodbye for now.'.format(guess))

def handle_incorrect_guess(guess, remaining_attempts):
    print('You guessed {0}, that is not my number. {1} attempts remaining'.format(guess, remaining_attempts))

def fail_to_win(selected_number):
    print('I\'m sorry! You failed to guess the secret number this time. It was {}.'.format(selected_number))

def check_guess_pattern(guess):
    result = re.match('^([1-9]|10){1}$', guess)
    if result:
        return True
    else:
        print("Please select a number 1 - 10.")

def main():
    attempts_remaining = 3
    random_number = random.randint(1, 10)

    print(instructions)
    while True:
        # Prompt user for guess
        user_guess = input(">> ")
        # Check that guess is a number 1-9 or 10.
        # Will print message if pattern match fails.
        if check_guess_pattern(user_guess):
            # Remove one attempt per guess
            attempts_remaining -= 1
            # Based on Guess:
            if user_guess == str(random_number):
                # Correct guess, break loop, end game
                handle_correct_guess(user_guess)
                return False
            elif attempts_remaining >= 1:
                # Incorrect guess, attempts still remaining
                handle_incorrect_guess(user_guess, attempts_remaining)
            else:
                # No attempts left, game over
                fail_to_win(random_number)
                return False
main()
