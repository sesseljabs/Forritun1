import string
piss = "research"
piss = list(piss)

for j in range(1,len(piss)-2,2):
    letter1 = piss[j]
    letter2 = piss[j+1]
    piss[j] = letter2
    piss[j+1] = letter1
print(*piss,sep="")

def main():
    # Your are NOT allowed to change this main function.
    filename = input("Enter name of file: ")
    file_object = open_file(filename)   
    if file_object is not None:
        scrambled_word_list = scramble_file_content(file_object)
        print_word_list(scrambled_word_list)
        file_object.close()
    else:
        print(f"File {filename} not found!")

# Your functions go here

def open_file(filename):
    try:
        f = open(filename, "r")
    except FileNotFoundError:
        f = None
    return f

def scramble_file_content(file_object):
    lines = file_object.readlines()
    newlines = []
    for i in lines:
        punct = ""
        i = i.strip()
        word = i
        if i[-1] in string.punctuation:
            punct = i[-1]
            i = i[:-1]
        if len(word)>3:
            word = list(i)
            for j in range(1,len(i)-2,2):
                letter1 = word[j]
                letter2 = word[j+1]
                word[j] = letter2
                word[j+1] = letter1
        else:
            word = i
        if punct != "":
            word += punct
        newlines.append("".join(word))
    return newlines


def print_word_list(word_list):
    for i in word_list:
        print(i,end=" ")

if __name__ == "__main__":
    main()