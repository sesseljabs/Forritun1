def decimal_to_binary(decimal):
    """Converts an integer from decimal to its binary representation."""

    # Fill in the missing code

    binString = ""
    if decimal == 0:
        binString += "0"
    while decimal >= 1:
        binString += str(decimal % 2)
        decimal = decimal // 2
    
    return binString[::-1]
print(decimal_to_binary(int(input())))