import json


def get_stored_username():
    """Get stored username if available."""

    filename = 'username.json'
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for new username"""

    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
    return username


def greet_user():
    """Greet user by name."""

    username = get_stored_username()
    if username:
        you = input(f"Is {username.title()} your name? (y or n) ")
        if you == 'y':
            print(f"Welcome back {username.title()}!")
        else:
            username = get_new_username()
            print(
                f"We'll remember you when you come back, {username.title()}!")
            return username
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username.title()}!")


greet_user()
