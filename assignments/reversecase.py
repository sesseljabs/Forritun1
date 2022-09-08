a_str = input("Enter a string: ")

# Complete the program below
for i in a_str:
    if i.islower():
        print(i.upper(),end="")
    elif i.isupper():
        print(i.lower(),end="")
    else:
        print(i, end="")
print()