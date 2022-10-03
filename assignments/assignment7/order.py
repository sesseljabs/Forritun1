def precedes(first, second):
    """Returns the string that comes first in lexicographical order.

    Ignores case.
    """
    # Your implementation goes here
    return sorted([first.lower(),second.lower()])[0]
print(precedes("abcdl", "abcde"))