a_str = input("Input a string: ") # Do not change this line

# Complete the program below
for i in range(len(a_str)):
    if i%2==0:
        print(a_str[i], end="")
print()