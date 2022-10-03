def main():
    m = int(input("Enter first number: "))
    n = int(input("Enter second number: "))
    if are_permutation_of_same_digits(m, n):
        print(f"The numbers {m} and {n} are permutations of each other.")
    else:
        print(f"The numbers {m} and {n} are not permutations of each other.")

def are_permutation_of_same_digits(num1: int, num2: int) -> bool:
    """Returns True if num1 and num2 are permutations of each other, False otherwise."""
    '''num1li,num2li=sorted(list(str(num1))),sorted(list(str(num2)))
    num2li=list(str(num2))
    num1li.sort()
    num2li.sort()'''
    return sorted(list(str(num1)))==sorted(list(str(num2)))

    # Implement this function.


# Feel free to break it down into more functions.


if __name__ == "__main__":
    main()
