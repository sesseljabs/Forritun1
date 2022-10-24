class Student:
    def __init__(self, first_name, last_name, id):
        """Initializes first and last name and the id"""
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __str__(self):
        """Formats first, last name and the id into a string """
        return f"{self.first_name} {self.last_name}, {self.id}"

class Course:
    def __init__(self, name):
        """Initializes name and empty student list"""
        self.name = name
        self.student_list = []

    def __str__(self):
        """Returns a string with the course name and list of all students"""
        return_string = f"{self.name}:"
        for i in self.student_list:
            return_string += f"\n{str(i):>40}"
        if self.name == "": # If the course name is empty it has been cleared
            return ""       # so then it doesn't print anything
        return return_string
    
    def add_student(self, student):
        """Adds given student to student list"""
        self.student_list.append(student)

    def remove_student(self, stud):
        """Removes given student from student list"""
        self.student_list.remove(stud)
        
    def clear(self):
        """Makes the course name blank and student list empty"""
        self.name = ""
        self.student_list = []

    def find_student_by_id(self, id):
        """Returns first student with given id"""
        for i in self.student_list:
            if i.id == id:
                return i
        