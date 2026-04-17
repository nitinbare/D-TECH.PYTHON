# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Derived class
class Student(Person):
    def __init__(self, name, age, student_id):
        super(). __init__(name, age)
        self.student_id = student_id

    def display_student(self):
        print("Student ID:", self.student_id)


# Derived class from Student
class GraduateStudent(Student):
    def __init__(self, name, age, student_id, degree):
        super(). __init__(name, age, student_id)
        self.degree = degree

    def display_graduate(self):
        print("Degree:", self.degree)


# Create object
g1 = GraduateStudent("Nitin", 23, 2334, "MCA")

# Call methods
g1.display_person()     # from Person
g1.display_student()    # from Student
g1.display_graduate()   # from GraduateStudent