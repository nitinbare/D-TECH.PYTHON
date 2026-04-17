class Student:
    def __init__(self):
        self.__name = ""
        self.__roll_no = 0 
        self.__marks = 0.0
        
    def set_name(self , name):
        if name.strip():
            self.__name = name
        else:
            print("Invalid name")
            
    def set_roll_no(self, roll_no):
        if roll_no.strip():
            self.__roll_no = roll_no
        else:
            print("Roll number must be positiv")
            
    def set_marks(self , marks):
        if 0<= marks <= 100:
            self._marks = marks
        else:
            print("Marks must be between 0 and 100")
            
    def get_name(self):
        return self.__name
    def get_roll_no(self):
        return self.__roll_no
    
    def get_marks(self):
        return self.__marks
# create object
s1 = Student()
s1.get_marks()
s1.get_name()
s1.get_roll_no()

print("Marks:", s1.get_marks())
print("Name:", s1.get_name())
print("Roll no:", s1.get_roll_no())