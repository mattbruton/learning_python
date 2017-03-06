# This is a simple script that will allow a user to add items to a shopping
# list. It's also the first one I've written in Python!

# Decorative text for use in instructions/preceding user's input:
prompt = '>> '
text_border = '=' * 80

# Helpful messages/instructions:
help_message = """
{0}
Shopping List\n
1. "SHOW" -- Prints items currently in your list.
2. "HELP" -- Brings you to this handy list of commands.
3. "DONE" -- Exits the program.
4. Anything else -- Adds your input to the list of things you need!
{0}""".format(text_border)

def run_todo():
    shopping_list = []
    while True:
        user_choice = input(prompt)
        if user_choice.lower() == 'done':
            show_then_exit(shopping_list)
            break
        elif user_choice.lower() == 'show':
            show_list(shopping_list)
        elif user_choice.lower() == 'help':
            show_help()
        else:
            add_item(shopping_list, user_choice)

def show_then_exit(list):
    print('{0}\nHere\'s what you need today:\n{0}'.format(text_border))
    show_list(list)

def show_help():
    print(help_message)

def add_item(list, item):
    list.append(item)
    item_text = 'item' if len(list) == 1 else 'items'
    print("Added {0}! List contains {1} {2}.".format(item, len(list), item_text))

def show_list(list):
    if len(list) > 0:
        list_to_string = ', '.join(list)
        print(list_to_string)
    else:
        print('Your list is empty!')

# Print initial instructions for the user
print(help_message)
# Handle user's input until they're ready to exit by typing "DONE".
run_todo()
