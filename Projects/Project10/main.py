from course import Student, Course

student1 = Student("John", "Lennon", "john@ru.is")
student2 = Student("Adele", "Adkins", "adele@ru.is")
student3 = Student("Paul", "McCartney", "paul@ru.is")
student4 = Student("Beyoncé", "Knowles", "beyoncé@ru.is")

student_list = [student1, student2, student3, student4]


course1 = Course("Programming")
for student in student_list:
    course1.add_student(student)


print()
print(course1)
course1.clear()
print(course1)


course2 = Course("Discrete Math")
for student in student_list:
    print(student)
    course2.add_student(student)
course2.remove_student(student3)
print()
print(course2)

