def get_formatted_name(first, last):
    """
    Creates formatted name.
    :param first: First name.
    :param last: Last name.
    :return: First and last name with capitalized first letters.
    """
    full_name = f"{first.title()} {last.title()}"
    return full_name
