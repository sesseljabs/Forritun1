"""A program that reads in a number n from the user, and prints out the first n squares."""

squares = []
n = int(input("Enter value for n: "))

for i in range(1, n + 1):
    squares.append(i ** 2)

print(f"The list of squares is {squares}.")
