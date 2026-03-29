"""
create two casses:

1. create shape class with methods input_Value() to take I and b
2. create reactangle class that inherits input_values and has one method
calculate_area() which prints area of reactangle"""
class Shape: # parent class
    def input_value(self,l, b):
        self.l= l
        self.b = b
        
class Reactangle(Shape): # child class
    def calculate_area(self):
        area = self.l * self.b
        print("Area of Reactangle: " , area)
        
r1 = Reactangle()
r1.input_value(5,3)
r1.calculate_area()


"""create a book class
    method set _detail (title,author)
    store and print the title and author
    
    class library
    overide method detail () with supper () keyword to call parent method
    add additional method show_book () that display "book available in library"""

class book:
    def show_details(self,title,author):
        self.title = title
        self.author = author
        print("Title:", self.title)
        print("Author : " , self.author)
        
class library(book):
    def set_details(self,title,author):
        super().show_details(title,author)
        print("Details store")
        
    def show(self):
        print("book available in library")
        
    def show(self):
        print("book available in library")
lib = library()
lib.set_details("Chava ,shivaji Swavant")
lib.show()
        