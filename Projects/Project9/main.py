import string

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
            if j[-1] in string.punctuation:
                j = j[:-1]
            parwords.append(j)
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


def main():
    f = open_file("test.txt")
    g = split_file_paragraphs(f)
    new = []
    counts = []
    for i in g:
        if i != []:
            words = split_to_words(i)
            new.append(words)
            counts.append(word_count(words))
    print(*new)
    print("\n\n")
    print(*counts,end="\n")
    

    
if __name__ == "__main__":
    main()