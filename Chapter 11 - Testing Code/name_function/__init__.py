def get_formatted_name(first, middle, last):
    """
    Creates formatted name.
    :param first: First name.
    :param middle: Middle name.
    :param last: Last name.
    :return: First and last name with capitalized first letters.
    """

    full_name = f"{first.title()} {middle.title()} {last.title()}"
    return full_name
