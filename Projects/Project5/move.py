MAX = 10
MIN = 1

position = 0

def move(dir, pos):
    pos = pos
    if dir == "r":
        if pos+1 <= MAX:
            pos += 1

    elif dir == "l":
        if pos-1 >= MIN:
            pos -= 1
    return pos

def printline(pos):
    for i in range(MIN,MAX+1):
        if i == pos:
            print("o",end="")
        else:
            print("x",end="")
    print()


position = int(input("Input a position between 1 and 10: "))
printline(position)
print('''l - for moving left
r - for moving right
Any other letter for quitting''')

choice = input("Input your choice: ").lower()
while choice == "r" or choice == "l":
    position = move(choice,position)
    printline(position)
    choice = input("Input your choice: ").lower()
printline(position)


'''
Input a position between 1 and 10: 7
xxxxxxoxxx
l - for moving left
r - for moving right
Any other letter for quitting
Input your choice: r
xxxxxxxoxx
Input your choice: r
xxxxxxxxox
Input your choice: r
xxxxxxxxxo
Input your choice: r
xxxxxxxxxo
Input your choice: l
xxxxxxxxox
Input your choice: l
xxxxxxxoxx
Input your choice: l
xxxxxxoxxx
Input your choice: l
xxxxxoxxxx
Input your choice: q
xxxxxoxxxx

'''
