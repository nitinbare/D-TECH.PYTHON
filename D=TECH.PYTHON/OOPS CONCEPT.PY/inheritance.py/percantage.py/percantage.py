class student:
    def __init__(self , name, eng,math,sci):
        self.name = name
        self.eng = eng
        self.math = math
        self.sci = sci
        
    def show(self):
        print("Name of student:" , self.name)
        print("Math of marks:" , self.math)
        print("eng marks:" , self.eng)
        
class Result(student):
    def show_result(self):
        super().show()
        total = (self.math + self.eng + self.sci)
        print("Total marks:" , total)
        percent= round((total/300)*100)
        print("You percentage:" , percent)
        if percent > 40:
            print("Congratulation !!! you'r passed the exam.")
            
        else:
            print("Oop ... you'r fali . best of luck for next exam")
        
r1 = Result("Priya" , 57,85,98)
r1.show_result()
        
    