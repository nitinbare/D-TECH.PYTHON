'''# 1

def Add(a,b):
    c = a+b
    return c
print(Add(10,20))

# 2
def Add(a,b):
    c = a+b
    print(c) 
print (Add(10,20))
'''

# user defined function
'''
def Greet():
    name = input("Enter your name:")
    print(f"Hello{name},How are you")
Greet()
'''

# paramitter function

'''def add(a,b):
    c = a+b
    print(c)
print(add(10,20))'''

# non parameter function
'''def add():
 a = int(input("Enter the furst no:"))
 b = int(input("E nter second no:"))
 c = a +b
 print(c)
add()'''

# parameter function
'''
def  rseven(n):
    if(n%2 ==0):
        print("Number is even:")
    else:
        print("Numbsr is odd:")
        rseven(10)
        rseven(11)'''

'''# non parameter function
def rseven():
    n = int(input("Enter a number: "))
    
    if( n % 2 == 0):
        print("Number is even")
    else:
        print("Number is odd")

rseven()
    
'''
#
'''def sum_avg(a, b, c):
    total = a + b + c
    avg = total / 3
    print("Sum:", total)
    print("Avg:", avg)

sum_avg(20, 40, 50)

'''
#
'''def sum_avg_palindrome(a,b,c):
    total = a +b +c
    avg = total / 3
    print("sum:",total)
    print("avg:",avg)

if str.total == str.total[::-1]:
    print("sum is palindrome")
else:
    print("sum is not palindrome")

sum_avg_palindrome(10,20,30)
'''
# argument
# 1
'''def sub(a,b):
    print(a-b)
sub(50,10)
sub(10,50)

# 2() name functuion)
def sample(name,age):
    print(f"My name is{name} and i am {age} years old. ..")

sample(20,"Patil")
sample("Patil",20)'''

# 3 default argument
'''def student(name ,age , school ="ABC school"):
    print("student details: ",name, age,school)
student("Nitin",15)
student("Rutu",11,"XYZ school")

# keyword argument

def students(name,age):
    print(f"My name is {name} and i am {age} years old")

student("Janavi" ,15)
student(name="Rutu" ,age=21)
student(age = 20,name="Pooja")
student(12,"Divya")'''

# ARGS Arguments
def percentage(sub1 ,sub2 ,sub3):
    avg = (sub1 + sub2 +sub3)/ 3
    print("Average: ",avg)
percentage(25,67,75)
def percentage(*args):
    sum = 0
    for i in args:
        sum = sum+i
    avg =sum / len(args)
    print("Average:" ,avg)

percentage(99,87,75,48)
percentage(98,45,58)

# arbitrary keywoerd argument = **kwargs

def stud(**kwargs):
    for sub in kwargs:
        sub_name=sub
        sub_marks=kwargs[sub]
        print(sub_name,"=",sub_marks)
    
stud(math = 58, eng=78,sci=88)
stud(math =58,eng=78,sci=88,marathi=95)

