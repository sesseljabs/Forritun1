def read_file(fname):
    '''
        Takes in file name and returns the file stream if it exists
        Returns None if the file does not exist
    '''
    try:
        f = open(fname,"r")
        return f
    except FileNotFoundError:
        return None

def read_parts(f):
    '''
        Takes in file stream and adds the parts of the grade to a list and returns it
    '''
    f = f.readlines()
    header = f[0].split()
    vals = f[1].split()
    parts = []

    for i in range(len(header)):
        # adds a tuple with the header and value to a list
        parts.append((header[i],float(vals[i])))

    return parts

def read_students(f):
    '''
        Takes file stream and parses the student grade list into a list
    '''
    f = f.readlines()
    students = []

    for i in f:
        i = i.split()
        for j in range(1,len(i[1:])+1): # this is to convert all strings with grades to float
            i[j] = float(i[j])
        students.append((i[0],i[1:])) # adds student id and a list of the grades to the student list
    return students

def calculate_grades(students,parts): # takes both lists and returns a nested list of student grades
    '''
        Takes in the list of student grades and parts of the grade
        Calculates each student's final grade
        Returns it in a list of the students grades
    '''
    newstudents = []
    value = [i[1] for i in parts]
    for i in students:
        total = 0
        for j in range(len(value)):
            # Multiplies each grade by its respective percentage to add to a total
            total += float(value[j])*float(i[1][j])
        newstudents.append((i[0],i[1],round(total,2))) # New tuple with the student id, student grades and total grade
    return newstudents

def print_grades(students,vals):
    '''
        Takes list of students and the parts of the grade and prints it nicely
    '''
    print(students)
    print()
    print(f"{'Student ID' : >16}",end="")
    # Grade type
    for i in vals:
        print(f"{i[0] : >14}", end="")
    print(f"{'Course grade' : >14}",end="")
    print()
    # Each student
    for i in students:
        print(f"{i[0] : >16}",end="")
        for j in i[1]: # Student's grades
            print(f"{j : >14}", end="")
        print(f"{i[2] : >14.2f}")

def main(): # main function
    partsinput = input("Enter filename for parts: ")
    values = read_file(partsinput)

    if values == None:
        print(f"File {partsinput} not found")
        return

    values = read_parts(values)
    print(values)

    valinput = input("Enter filename for grades: ")
    students = read_file(valinput)

    if students == None:
        print(f"File {valinput} not found")
        return
        
    students = read_students(students)
    print(students)

    grades = calculate_grades(students, values)

    print_grades(grades, values)

if __name__ == "__main__":
    main()