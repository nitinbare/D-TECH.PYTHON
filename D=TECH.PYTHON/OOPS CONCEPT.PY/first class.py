# creating a class student having attributes
# name and age
'''
class Student:
    def __init__(self , name,age):
        self.name = name
        self.age = age
        
    def info(self):
        print(f"My name is {self.name} and I am {self.age} year old")
        
s = Student("Nitin" , 23)
s.info()

s1 = Student("Komal" , 26)
s1.info()
        '''

# create a method percentage which display percentage of the student
'''class Marks:
     def __init__(self,sub1,sub2,sub3):
         self.sub1 = sub1
         self.sub2 = sub2
         self.sub3 = sub3
     def Percentage(self):
         total = (self.sub1 + self.sub2 + self.sub3)
         print("Percentage:" , round((total /300)*100))
         
m = Marks(98,56,54)
m.Percentage()

m1 = Marks(45,25,65)
m1.Percentage()
            '''
            
# take student info from user input

'''class Student:
    def __init__(self , name, age):
        self.name = name
        self.age = age
        
    def display(self):
        print(f"Nmae of the student : {self.name}")
        print(f"Age of student:{self.age}")
        
# taking input from user
name = input("Enter student name:")
age = int(input("Enter age of student:"))

s1 = Student(name , age)
s1.display()
          '''
          
# creat a class reactangle for calculating
# area of reactangle

class Reactangle:
    def __init__(self , l ,b):
        self.l = l
        self.b = b
    
    def area (self):
        print("Area of reactange: ", self.l * self.b)
        
res1 = Reactangle(20,30)
res1.area()

