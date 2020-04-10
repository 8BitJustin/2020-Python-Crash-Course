def get_formatted_name(first, last):
    """
    Generate a neatly formatted full name.
    :param first: First name
    :param last: Last name
    :return: First name and last name together (ex. Justin Saturno)
    """
    full_name = f"{first.title()} {last.title()}"
    return full_name


print(get_formatted_name("justin", "olson"))
