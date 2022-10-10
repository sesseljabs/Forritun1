def read_file(fname): # takes filename and returns lines
    try:
        f = open(fname,"r")
        return f
    except FileNotFoundError:
        return None

def read_parts(f): # return list of tuples
    f = f.readlines()
    header = f[0].split()
    vals = f[1].split()
    li = []

    for i in range(len(header)):
        li.append((header[i],float(vals[i])))

    return li

def read_students(f): # return list of tuples
    f = f.readlines()
    students = []

    for i in f:
        i = i.split()
        for j in range(1,len(i[1:])+1):
            i[j] = float(i[j])
        students.append((i[0],i[1:]))
    return students

def calculate_grades(students,parts): # takes both lists and returns a nested list of student grades
    newstudents = []
    value = [i[1] for i in parts]
    for i in students:
        total = 0
        for j in range(len(value)):
            total += float(value[j])*float(i[1][j])
        newstudents.append((i[0],i[1],round(total,2)))
    return newstudents

def print_grades(students,vals):
    '''prints grades :) '''
    print(students)
    print()
    print(f"{'Student ID' : >16}",end="")
    for i in vals:
        print(f"{i[0] : >14}", end="")
    print(f"{'Course grade' : >14}",end="")
    print()
    for i in students:
        print(f"{i[0] : >16}",end="")
        for j in i[1]:
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