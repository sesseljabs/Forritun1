def main():
    word = input("Enter a word to be added to the list: ")
    words = []
    while word != "x":
        words.append(word)
        word = input("Enter a word to be added to the list: ")
    print(words)
    
    if len(words)>0:
        letter = words[0][0]

    for i in words:
        if i[0]==letter:
            print(i)
            letter = i[-1]


# Your functions should appear here


if __name__ == "__main__":
    main()


'''
Enter a word to be added to the list: arm
Enter a word to be added to the list: mom
Enter a word to be added to the list: dog
Enter a word to be added to the list: giraffe
Enter a word to be added to the list: mouse
Enter a word to be added to the list: elephant
Enter a word to be added to the list: trunk
Enter a word to be added to the list: sing
Enter a word to be added to the list: kangaroo
Enter a word to be added to the list: x
['arm', 'mom', 'dog', 'giraffe', 'mouse', 'elephant', 'trunk', 'sing', 'kangaroo']
arm
mom
mouse
elephant
trunk
kangaroo
'''