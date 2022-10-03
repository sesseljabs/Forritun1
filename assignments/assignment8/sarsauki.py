'''

I'm going to make a list with every tile and where you can go from there
There's probably a better way to do this (such as keeping only track of the walls) but i don't do better ways

There is a variable to track current position

Then i make some functions to change the location depending on input to make everything simpler
then just run it in a while loop that stops when location is the same as defined victory point

'''

VICTORY = (2,0)

locX, locY = 0, 0


def move(x,y,dir):
    if dir=="n":
        return (x, y+1)
    elif dir=="s":
        return (x, y-1)
    elif dir=="w":
        return (x-1, y)
    elif dir=="e":
        return (x+1, y)
    else:
        return (x,y)

def getName(l):
    if l == "n":
        return "(N)orth"
    elif l == "s":
        return "(S)outh"
    elif l == "w":
        return "(W)est"
    elif l == "e":
        return "(E)ast"

def options(dirs):
    string = getName(dirs[0])

    if len(dirs)>1:
        for i in range(1, len(dirs)):
            string += " or "
            string += getName(dirs[i])
    string += ". "
    return string


# 1,1 1,2 1,3
# 2,1 2,2 2,3
# 3,1 3,2 3,3
# but in the program the grid will be from 0 to 2
# order: nesw so codingrooms accepts the answer

grid = [ 
    [ "n" , "nes" , "es" ],
    [ "n" , "sw" , "ew" ],
    [ "n" , "ns" , "sw" ]
]

choice = ""


while  locX != VICTORY[0] or locY != VICTORY[1]:
    print("You can travel: "+options(grid[locX][locY]))
    choice = input("Direction: ").lower()

    if choice in grid[locX][locY] and len(choice)==1:
        locX, locY = move(locX, locY, choice)
    else:
        print("Not a valid direction!")
    
print("Victory!")
