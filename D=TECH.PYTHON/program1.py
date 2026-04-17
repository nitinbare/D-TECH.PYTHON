''' create a hybrid inheritance structure where:

1. schoool - method - school_info() which prints 
"Name: Green valley high school"

2. Teacher - (inherits from school)-  having method teach_Sub()
which prints "Teaching mathematics".

3. SportCoach - method train_sports() which prints "training footboall"

4. student - inherits from teacher and sportcoach-
method -study() prints "studying for exams"

5. juniorStudent - inherits from students - having method
participate_Event() which prints "participating in cultural events"'''


class school:
    def school_info(self):
        print("Green valley high school")
        
class Teacher(school):
    def teach_Sub(self):
        print("Teaching mathematics")
   
class SportCoach:
    def train_sport(self):
        print("training footboall")
        
class student(Teacher, SportCoach):
    def study(self):
        print("studying for exam")
        
class juniorStudent(student):
    def Paritici_Event(self):
        print("participating in cultural event")
        
g = juniorStudent()

g.Paritici_Event()
g.school_info()
g.teach_Sub()
g.train_sport()
g.study()
