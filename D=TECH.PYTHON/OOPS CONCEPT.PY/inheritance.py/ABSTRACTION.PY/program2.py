from abc import ABC,abstractmethod
class Shape(ABC):
    
    @abstractmethod
    def area (self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
class Rectangle(Shape):
        def __init__(self , l ,b):
            self.l = l
            self.b = b
            
        def area(self):
            return self.l * self.b
        
        def perimeter(self):
            return 2 *(self.l + self.b)
        
class Circle(Shape):
    def __init__(self,rad):
        self.rad = rad
        
    def area(self):
        return 3.14 * self.rad **2
    
    def perimeter(self):
        return 2* 3.14 * self.rad
    
rec=Rectangle(5,3)
print("Area of reactangle:",rec.area())
print("Perimeter of rectangle:", rec.perimeter())
c = Circle(3)
print("Area of circle:", c.area())
print("perimeter of circle:" , c.perimeter())
        
        