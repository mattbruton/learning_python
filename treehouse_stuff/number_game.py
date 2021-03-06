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
    print('Yay! You guessed {}, that was the secret number!'.format(guess))

def handle_incorrect_guess(guess, remaining_attempts):
    print('You guessed {0}, that is not my number. {1} attempts remaining'.format(guess, remaining_attempts))

def fail_to_win(selected_number):
    print('I\'m sorry! You failed to guess the secret number this time. It was {}.'.format(selected_number))

def give_hint(guess, actual_number):
    comparison_word = 'less' if actual_number < int(guess) else 'greater'
    print('Hint: The number is {} than your guess.'.format(comparison_word))

def check_for_continue():
    user_response = input("Want to play again? (Y/n)\n>> ")
    return user_response.lower() in list(['y', 'yes', ''])

def check_guess_pattern(guess):
    result = re.match('^([1-9]|10){1}$', guess)
    return True if result else print("Please select a number 1 - 10.")

def game():
    attempts_remaining = 2
    random_number = random.randint(1, 10)
    while True:
        user_guess = input(">> ")
        if check_guess_pattern(user_guess):
            if user_guess == str(random_number):
                handle_correct_guess(user_guess)
                return False
            elif attempts_remaining >= 1:
                handle_incorrect_guess(user_guess, attempts_remaining)
                give_hint(user_guess, random_number)
                attempts_remaining -= 1
            else:
                fail_to_win(random_number)
                return False

def main():
    while True:
        print(instructions)
        game()
        if check_for_continue() == False:
            break
    print('Bye for now!')

main()
