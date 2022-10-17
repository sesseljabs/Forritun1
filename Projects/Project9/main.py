import string
from operator import itemgetter

def open_file(fname):
    '''Opens file by name, returns filestream and None if file doesn't exist'''
    try:
        f = open(fname,"r")
        return f
    except FileNotFoundError:
        return None

def split_file_paragraphs(f):
    '''Takes in file object and splits into paragraphs'''
    lines = f.readlines()
    paragraphs = [[]]
    currentpar = 0
    for i in range(len(lines)):

        if lines[i] != "\n":
            paragraphs[currentpar].append(lines[i])
        else:
            currentpar+=1
            paragraphs.append([])
    return paragraphs

def split_to_words(paragraph):
    '''Takes in one paragraph and turns it into a list of all the words, stripped of punctuation'''
    parwords = []
    for i in paragraph:
        line = i.split()
        for j in line:
            if j[0] in string.punctuation:
                j = j[1:]
            if j[0] in string.punctuation:
                j = j[1:]
            if j[-1] in string.punctuation:
                j = j[:-1]
            if j[-1] in string.punctuation:
                j = j[:-1]
            parwords.append(j.lower())
    return parwords

def word_count(words):
    counts = dict()

    for word in words:
        word = word.lower()
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

def get_all_words(text):
    allwords = []
    for i in text:
        for j in i:
            allwords.append(j)
    return allwords



def get_par_allwords(paragraphs):
    pars = dict()

    for i in range(len(paragraphs)):
        for j in paragraphs[i]:
            if j in pars:
                if i+1 not in pars[j]:
                    pars[j].append(i+1)
            else:
                pars[j] = [i+1]
    return pars

def split_all_paragraphs(paragraphs):
    splitpars = []
    for i in paragraphs:
        splitpars.append(split_to_words(i))
    return splitpars

def print_highest(allwords,number):
    print()
    print(f"The highest {number} counts: ")

    count = word_count(allwords)


    sortedcount = sorted(list(sorted(count.items())), key=itemgetter(1), reverse=True)

    for i in range(number):
        print(f"{sortedcount[i][0]}: {sortedcount[i][1]}")


def print_locations(paragraph_location):
    print()
    print("The paragraph index: ")
    locs = sorted(list(paragraph_location.items()))
    for i in locs:
        print(i[0], end=" ")
        print(*i[1], sep=", ")


def main():
    fname = input("Enter filename: ")
    f = open_file(fname)
    if f == None:
        print(f"Filename {fname} not found!")
        return

    paragraphs = split_file_paragraphs(f)
    splitpars = split_all_paragraphs(paragraphs)

    paragraph_location = get_par_allwords(splitpars)
    print_locations(paragraph_location)

    
    print_highest(get_all_words(splitpars), 10)
    print_highest(get_all_words(splitpars), 20)
    


    #print(sorted(list(sorted(allwordcount.items())), key=itemgetter(1), reverse=True))
    
    

    
if __name__ == "__main__":
    main()