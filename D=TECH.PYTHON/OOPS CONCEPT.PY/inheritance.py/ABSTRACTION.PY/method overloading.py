#method overloading dont suport in python
'''class Addition:
    def add(self ,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        print(self.a+ self.b.c)
        
class subtraction(Addition):
    def add(self,a,b):
        self.a = a
        self.b = b
        print(self.a + self.b)
        
obj = subtraction()
obj.add(10,20)
obj.add(10,20,30)'''


#
'''class Math_operation:
    def add(self,*args):
        Total = 0
        for num in args:
            Total +=num
            
        return Total
    
math = Math_operation()
print(math.add(2,3))
print(math.add(1,2,3))
print(math.add(10,20,30,40))'''

# method overriding

'''class Animal:
    def speak(self):
        print("Animals make sound")
        
class dog(Animal):
    def speak(self):
        print("do barks")
        
class cat(Animal):
    def speak(self):
        print("Cat Meow")
        
d1 = dog()
d1.speak()
c1  = cat()
c1.speak()'''
