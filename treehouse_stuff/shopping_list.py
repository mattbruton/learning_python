# This is a simple script that will allow a user to add items to a shopping
# list. It's also the first one I've written in Python!

# Decorative text for use in instructions/preceding user's input:
prompt = '>> '
text_border = '=' * 80

# Helpful messages/instructions:
instructions = """{0}
Ready to add items to your shopping list?
Simply type an item you need and press enter to add it to your list.
Type "DONE" to exit, "SHOW" to see your current list, or "HELP" for all options.
{0}""".format(text_border)

help_message = """
{0}
List of Commands:\n
1. "SHOW" -- Prints items currently in your list.
2. "HELP" -- Brings you to this handy list of commands.
3. "DONE" -- Exits the program.
4. Anything else -- Adds your input to the list of things you need!
{0}""".format(text_border)

def run_todo():
    shopping_list = []
    while True:
        user_choice = input(prompt)
        if user_choice == 'DONE':
            show_then_exit(shopping_list)
            break
        elif user_choice == 'SHOW':
            show_list(shopping_list)
        elif user_choice == 'HELP':
            show_help()
        else:
            shopping_list.append(user_choice)

def show_then_exit(list):
    print('{0}\nHere\'s what you need today:\n{0}'.format(text_border))
    show_list(list)

def show_help():
    print(help_message)

def show_list(list):
    if len(list) > 0:
        list_to_string = ', '.join(list)
        print(list_to_string)
    else:
        print('Your list is empty!')

# Print initial instructions for the user
print(instructions)
# Handle user's input until they're ready to exit by typing "DONE".
run_todo()
