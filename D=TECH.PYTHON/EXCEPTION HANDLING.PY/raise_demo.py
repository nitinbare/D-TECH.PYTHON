'''age = int(input("enter your age:"))
try:
    if age<0:
        raise ValueError("Age cannot be ngative")
        print("Enter valid age")
        
    else:
        print(f"Your age is {age}")
        
finally:
    print("Program excuted sucesfully")

'''
# write a program that handels divition and actches divition by zero
'''
try:
    a = int(input("Enter numerator:"))
    b = int(input("Enter denominator:"))
    result = a /b
    print("Result:", result)
    
except ZeroDivisionError:
    print(" Cannot divide by zero.")
    
except ValueError:
    print("Please enter valid numbers.")'''
    
# Create a custom exception if age is below 18.

class UnderAgeError(Exception):
    pass
age = int(input("Enter your age:"))

try:
    if age <18:
        raise UnderAgeError("you must be 18 or old.")
    print("Access granted.")
    
except UnderAgeError as e:
    print("Access denied:" ,e)