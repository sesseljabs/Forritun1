def isPermutation(num1: int, num2: int) -> bool:
    return sorted(list(str(num1)))==sorted(list(str(num2)))

def main():
    hi_end = int(input("Enter high end of search interval: "))
    for candidate in range(10, hi_end + 1):
        if is_permutative(candidate):
            print(candidate)


def is_permutative(number: int) -> bool:
    """Returns True if number is permutative, False otherwise."""
    isPerm = True
    for i in range(1,len(str(number))+1):
        if not isPermutation(number, number*i):
            isPerm = False
    return isPerm


# Feel free to add more functions here below.
# You should reuse functions from previous question if you can.


if __name__ == "__main__":
    main()
