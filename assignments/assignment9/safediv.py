def main():
    num1_str = input("Input first number: ")
    num2_str = input("Input second number: ")

    result = divide_safe(num1_str, num2_str)

    # TODO: Display the result.
    print(result)

def divide_safe(num1_str, num2_str):
    """Returns num1/num2 if the input is valid, else None."""

    try:
        return round(float(num1_str)/float(num2_str),5)
    except ValueError:
        return None
    except ZeroDivisionError:
        return None


if __name__ == "__main__":
    main()
