'''class Student:
    def __init__(self , name, std, percent):
        self.name = name
        self.std = std
        self.percent = percent
        
    def get_percent(self):
        return self.__percent
    
    def display(self):
        print(f"{self.name} is in class{self.std} with{self.__percent +2} %)")
        
stud = Student("Raghav" , 21,93)
stud.display()
    
'''

# getter and setter

class Student:
    def __init__(self):
        self.__marks = 0 # private
        
       # setter method 
    def set_marks(self , m):
        if 0 <= m <= 100:
            self.__marks = m
        else:
            print("Invalid marks!")
            
            # getter method
    def get_marks(self):
        return self.__marks
    
s = Student()
s.set_marks(85)
print(s.get_marks())
        
            
            
            