a_str = input("Input a string: ")
char_to_count = input("Input a character to count: ")

# Complete the program below


for i in range(len(a_str)):
    if a_str[i] == char_to_count:
        print(i)