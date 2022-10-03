def is_float(string_to_test):
    """Returns True if the given string is a float, otherwise False."""

    # TODO: Add your implementation here.

    try:
        float(string_to_test)
        return True
    except ValueError:
        return False

# Example usage
print(is_float("3.45"))
print(is_float("abc"))
