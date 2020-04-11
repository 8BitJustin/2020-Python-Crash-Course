def get_formatted_name(first, last, middle=""):
    """
    Creates formatted name.
    :param first: First name.
    :param middle: Middle name.
    :param last: Last name.
    :return: First and last name with capitalized first letters.
    """

    if middle:
        full_name = f"{first.title()} {middle.title()} {last.title()}"
    else:
        full_name = f"{first.title()} {last.title()}"

    return full_name

# Test
# print(get_formatted_name('justin', 'olson'))
# print(get_formatted_name('justin', 'olson', 'richard'))
