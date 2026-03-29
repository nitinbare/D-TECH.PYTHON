#Create a parent class School (school name , location).Create a two child
# classes: Teacher (subject , salary) and Student (grade, roll number).
# create objects of both and print their details.

'''class School:
    def __init__(self, name , location):
        self.name = name
        self.location = location
        
    def school_info(self):
        print("School Name:" , self.name)
        print("Location:", self.location)
        
class Teacher(School):
    def __init__(self, name, location, subject, salary):
        super().__init__(name, location)
        self.subject = subject
        self.salary = salary
    def teacher_info(self):
        self.school_info()
        print("Subject:", self.subject)
        print("Salary:" , self.salary)
        
class Student(School):
    def __init__(self, name, location, grade, roll_number):
        super().__init__(name, location)
        self.grade= grade
        self.roll_number = roll_number
        
    def student_info(self):
        self.school_info()
        print("Grade:" , self.grade)
        print("Roll Number:" , self.roll_number)
    
    
    # create object
    
t1 = Teacher("ABC School", "New York", "Mathematics" , 50000)
s1 = Student("ABC School", "New York" , "5th", 101)
    
print("Teacher Details:")
t1.teacher_info()
print("\nStudent Details:")
s1.student_info()
'''

# Multiple inheritance

'''
create the following classes:
person : prints - name and age
Address : prints - address
Student : prints - college name
'''

'''class person:
    def info(self):
        print("Name: Priti")
        print("Age: 23")
        
class Address:
    def location(self):
        print("City: pune")
        print("Country: India")
        
class Student(person,Address):
    def stud_info(self):
        print("College name: MIT Punr")

s = Student()
s.info()
s.location()
s.stud_info()'''
        
# Q
'''
create a following classes:
reactangle : which print area of reactangle
triangle : which prints area of triangle
calculator : inherit both
create calculator object and call both area() methods
'''
class Reactangle:
    def rec_area(self, l, b):
        return l*b
class Trangle:
    def triangle_area(self,b,h):
        return 0.5 * b*h
    
class Calculator (Reactangle, Trangle):
    pass
c = Calculator()
print("Area of reactangle:" , c.rec_area(10,20))
print("Area of Triangle:", c.triangle_area(10,5))